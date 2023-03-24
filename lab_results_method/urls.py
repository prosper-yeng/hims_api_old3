from django.urls import path
from rest_framework import routers
from .views import LabResultsMethodViewSet

router = routers.DefaultRouter()
router.register("api/lab_results_method", LabResultsMethodViewSet, "lab_results_method")

urlpatterns = router.urls
