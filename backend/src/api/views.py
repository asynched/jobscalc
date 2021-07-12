from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import (
    JobSerializer,
    PlanningSerializer,
    ProfileSerializer,
    RegisterSerializer,
)

from core.models import Job, Planning, Profile


class JobViewset(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        profile: Profile = self.request.user
        queryset = Job.objects.filter(profile=profile)

        return queryset

    def perform_create(self, serializer: JobSerializer):
        profile: Profile = self.request.user

        price = (
            profile.planning.hourly_value
            * serializer.validated_data["estimated_completion_time"]
        )

        serializer.save(profile=profile, price=price)

    @action(
        methods=["get"],
        permission_classes=[permissions.IsAuthenticated],
        detail=False,
        url_path="data",
        url_name="jobs_data",
    )
    def get_jobs_info(self, request):
        profile = self.request.user

        total = Job.objects.filter(profile=profile).count()
        in_progress = Job.objects.filter(profile=profile, finished=False).count()
        finished = Job.objects.filter(profile=profile, finished=True).count()

        response_data = {
            "total": total,
            "in_progress": in_progress,
            "finished": finished,
        }

        return Response(response_data)


class PlanningRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = PlanningSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset)

        return obj

    def get_queryset(self):
        profile: Profile = self.request.user
        queryset = Planning.objects.filter(profile=profile)

        return queryset

    def perform_create(self, serializer):
        profile: Profile = self.request.user
        serializer.save(profile=profile)


class ProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset)

        return obj

    def get_queryset(self):
        user: Profile = self.request.user

        queryset = Profile.objects.filter(pk=user.pk)

        return queryset


class RegisterView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer
