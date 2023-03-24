from django.urls import path
from rest_framework import routers
from .views import MedicationDosageViewSet

router = routers.DefaultRouter()
router.register("api/medication_dosage", MedicationDosageViewSet, "medication_dosage")

urlpatterns = router.urls
