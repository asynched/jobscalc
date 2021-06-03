from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import JobViewset, PlanningRetrieveUpdateView, ProfileRetrieveUpdateView, RegisterView

router = DefaultRouter()

router.register(r"jobs", JobViewset, basename="jobs")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("register/", RegisterView.as_view()),
    # path("auth/", include("rest_framework.urls")),
    path("planning/", PlanningRetrieveUpdateView.as_view()),
    path("profile/", ProfileRetrieveUpdateView.as_view()),
]
