from django.urls import path
from rest_framework import routers
from .views import LabTestResultsUploadViewSet

router = routers.DefaultRouter()
router.register(
    "api/lab_test_results_upload",
    LabTestResultsUploadViewSet,
    "lab_test_results_upload",
)

urlpatterns = router.urls
