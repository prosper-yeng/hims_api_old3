# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import ImmunizationsViewSet, CombinedUserPatientImmunizationsView

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/immunizations", ImmunizationsViewSet, "immunizations")

urlpatterns = [
    path(
        "api/patient_immunizations_list",
        CombinedUserPatientImmunizationsView.as_view(),
        name="patient_immunizations_list",
    ),
]
urlpatterns += router.urls
