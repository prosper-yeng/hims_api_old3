from django.urls import path
from rest_framework import routers
from .views import PrescriptionViewSet, CombinedDiagnosisPrescriptionView

router = routers.DefaultRouter()
router.register("api/prescription", PrescriptionViewSet, "prescription")


urlpatterns = [
    path(
        "api/diagnosis_prescription_list",
        CombinedDiagnosisPrescriptionView.as_view(),
        name="diagnosis_prescription_list",
    ),
]
urlpatterns += router.urls
