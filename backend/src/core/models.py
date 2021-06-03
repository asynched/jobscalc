from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from core.helpers import calculate_default_date


class CustomAccountManager(BaseUserManager):
    # If you have any other required parameters it should recieve it here
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    # Required identifier (can be watever you want)
    email = models.EmailField(max_length=64, unique=True)

    # Optional fields
    name = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.URLField(max_length=255, null=True, blank=True,
                                default="https://scontent-gru1-2.xx.fbcdn.net/v/t1.30497-1/143086968_2856368904622192_1959732218791162458_n.png?_nc_cat=1&ccb=1-3&_nc_sid=7206a8&_nc_ohc=59lRIs-xu-gAX8xZlk0&tn=iEB9roOiVPhoqnVA&_nc_ht=scontent-gru1-2.xx&oh=31a3b67eabeee51497401a9e5771d920&oe=60DC1578")

    # Required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Required identified, must be unique and declared in your model
    USERNAME_FIELD = "email"

    # Boiler plate
    objects = CustomAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin or self.is_superuser

    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=Profile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Planning.objects.create(
            profile=instance
        )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.planning.save()


class Planning(models.Model):
    expected_montly_payment = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)
    daily_worktime = models.IntegerField(default=0)
    weekly_worktime = models.IntegerField(default=0)
    yearly_vacation_weeks = models.IntegerField(default=0)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def hourly_value(self):
        value = self._calculate_hourly_value()

        return value

    def _calculate_hourly_value(self):
        MONTHLY_PAYMENT = float(self.expected_montly_payment)
        WORKTIME_DAILY = self.daily_worktime
        WORKTIME_WEEKLY = self.weekly_worktime
        VACATION_WEEKS = self.yearly_vacation_weeks

        WEEKS_PER_YEAR = 52
        WEEKS_PER_MONTH = (WEEKS_PER_YEAR - VACATION_WEEKS) / 12
        WEEK_TOTAL_HOURS = WORKTIME_DAILY * WORKTIME_WEEKLY

        MONTHLY_TOTAL_HOURS = WEEK_TOTAL_HOURS * WEEKS_PER_MONTH

        if not MONTHLY_TOTAL_HOURS:
            MONTHLY_TOTAL_HOURS = 1

        HOURLY_VALUE = MONTHLY_PAYMENT / MONTHLY_TOTAL_HOURS

        return HOURLY_VALUE

    def __str__(self):
        return str(self.profile)


class Job(models.Model):
    name = models.CharField(max_length=255)
    daily_hours = models.IntegerField(default=1)
    estimated_completion_time = models.IntegerField(default=12)
    finished = models.BooleanField(default=False)
    due_date = models.DateField(default=calculate_default_date)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
