from django.urls import path
from rest_framework import routers
from .views import LabTestResultsCategoryViewSet

router = routers.DefaultRouter()
router.register(
    "api/lab_test_results_category",
    LabTestResultsCategoryViewSet,
    "lab_test_results_category",
)

urlpatterns = router.urls
