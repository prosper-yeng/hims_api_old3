from django.urls import path
from rest_framework import routers
from .views import LabTestResultsParametersViewSet

router = routers.DefaultRouter()
router.register(
    "api/lab_test_results_parameters",
    LabTestResultsParametersViewSet,
    "lab_test_results_parameters",
)

urlpatterns = router.urls
