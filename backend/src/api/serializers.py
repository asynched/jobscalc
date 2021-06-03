from rest_framework import serializers
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from core.models import Job, Planning, Profile


class JobSerializer(serializers.ModelSerializer):
    price = serializers.ReadOnlyField()

    class Meta:
        fields = [
            "id",
            "name",
            "daily_hours",
            "estimated_completion_time",
            "finished",
            "due_date",
            "price",
        ]

        model = Job


class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "expected_montly_payment",
            "daily_worktime",
            "weekly_worktime",
            "yearly_vacation_weeks",
            "hourly_value",
        ]

        model = Planning


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "image_url",
            "name",
        ]

        model = Profile


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Profile.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Profile
        fields = ('password',
                  'email', 'name')
        extra_kwargs = {
            'name': {'required': True},
        }

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        profile = Profile.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
        )

        profile.set_password(validated_data['password'])
        profile.save()

        return profile
