from django.urls import path
from rest_framework import routers
from .views import CombinedPatientServiceChargeView, PatientServiceChargeViewSet

router = routers.DefaultRouter()
router.register(
    "api/patient_service_charge", PatientServiceChargeViewSet, "patient_service_charge"
)

# urlpatterns = router.urls
urlpatterns = [
    path(
        "api/patient_service_charge_list",
        CombinedPatientServiceChargeView.as_view(),
        name="patient_service_charge_list",
    ),
]
urlpatterns += router.urls
