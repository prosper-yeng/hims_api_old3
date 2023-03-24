# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import SocialHistoryViewSet, CombinedUserPatientSocialHistoryView

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/social-history", SocialHistoryViewSet, "social_history")


urlpatterns = [
    path(
        "api/patient_social_history_list",
        CombinedUserPatientSocialHistoryView.as_view(),
        name="patient_social_history_list",
    ),
]
urlpatterns += router.urls