from django.urls import path
from rest_framework import routers
from .views import (
    ConsultationDiagnosisViewSet,
    ConsultationDiagnosisDetailViewSet,
    CombinedConsultedDiagnosedPatientView,
)

router = routers.DefaultRouter()
router.register(
    "api/consultation_diagnosis", ConsultationDiagnosisViewSet, "consultation_diagnosis"
)
router.register(
    "api/consultation_diagnosis_detail",
    ConsultationDiagnosisDetailViewSet,
    "consultation_diagnosis_detail",
)
# urlpatterns = router.urls

urlpatterns = [
    path(
        "api/consulted_diagnosed_patient_list",
        CombinedConsultedDiagnosedPatientView.as_view(),
        name="consulted_diagnosed_patient_list",
    ),
]
urlpatterns += router.urls
