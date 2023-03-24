from django.urls import path
from rest_framework import routers
from .views import (
    ConsultationViewSet,
    ConsultationDetailViewSet,
    CombinedConsultationVitalSignView,
)

router = routers.DefaultRouter()
router.register("api/consultation", ConsultationViewSet, "consultation")
router.register(
    "api/consultation_detail", ConsultationDetailViewSet, "consultation_detail"
)
# urlpatterns = router.urls


urlpatterns = [
    path(
        "api/consultated_patient_list",
        CombinedConsultationVitalSignView.as_view(),
        name="consultated_patient_list",
    ),
]
urlpatterns += router.urls
