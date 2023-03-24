# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import InterHospitalPatientTransferViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register(
    "api/inter_hospital_patient_transfer",
    InterHospitalPatientTransferViewSet,
    "inter_hospital_patient_transfer",
)

urlpatterns = router.urls
