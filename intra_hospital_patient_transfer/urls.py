# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import IntraHospitalPatientTransferViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register(
    "api/intra_hospital_patient_transfer",
    IntraHospitalPatientTransferViewSet,
    "intra_hospital_patient_transfer",
)

urlpatterns = router.urls
