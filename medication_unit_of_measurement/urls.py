from django.urls import path
from rest_framework import routers
from .views import MedicationUnitOfMeasurementViewSet

router = routers.DefaultRouter()
router.register(
    "api/medication_unit_of_measurement",
    MedicationUnitOfMeasurementViewSet,
    "medication_unit_of_measurement",
)

urlpatterns = router.urls
