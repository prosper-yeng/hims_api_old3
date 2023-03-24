from django.urls import path
from rest_framework import routers
from .views import PrescriptionDosageViewSet

router = routers.DefaultRouter()
router.register(
    "api/prescription_dosage", PrescriptionDosageViewSet, "prescription_dosage"
)

urlpatterns = router.urls
