from django.urls import path
from rest_framework import routers
from .views import (
    VitalSignViewSet,
    VitalSignDetailViewSet,
    CombinedPatientVitalSignView,
)

router = routers.DefaultRouter()
router.register("api/vital_sign", VitalSignViewSet, "vital_sign")
router.register("api/vital_sign_detail", VitalSignDetailViewSet, "vital_sign_detail")


urlpatterns = [
    path(
        "api/patient_vitalsign_list",
        CombinedPatientVitalSignView.as_view(),
        name="patient_vitalsign_list",
    ),
]
urlpatterns += router.urls
