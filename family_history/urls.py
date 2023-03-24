# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import FamilyHistoryViewSet, CombinedUserPatientFamilyHistoryView

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/family-history", FamilyHistoryViewSet, "family_history")

urlpatterns = [
    path(
        "api/patient_family_history_list",
        CombinedUserPatientFamilyHistoryView.as_view(),
        name="patient_family_history_list",
    ),
]
urlpatterns += router.urls