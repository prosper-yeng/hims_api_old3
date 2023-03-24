from django.urls import path
from rest_framework import routers
from .views import LabTestResultsTypeViewSet

router = routers.DefaultRouter()
router.register(
    "api/lab_test_results_type", LabTestResultsTypeViewSet, "lab_test_results_type"
)

urlpatterns = router.urls
