from django.contrib.auth.admin import UserAdmin

from django.contrib import admin

from core.forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile, Planning, Job

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm

    list_display = ("email", "name", "date_joined", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("name",)}),
        ("Permissions", {"fields": ("is_admin",)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "name", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


@admin.register(Planning)
class PlanningAdmin(admin.ModelAdmin):
    list_display = [
        "expected_montly_payment",
        "daily_worktime",
        "weekly_worktime",
        "yearly_vacation_weeks",
        "profile",
        "created_at",
        "updated_at",
        "hourly_value",
    ]


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "daily_hours",
        "estimated_completion_time",
        "finished",
        "due_date",
        "profile",
        "price",
    ]
