# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import MedicationAdministrationViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register(
    "api/medication_administration",
    MedicationAdministrationViewSet,
    "medication_administration",
)

urlpatterns = router.urls
