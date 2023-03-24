from django.urls import path
from rest_framework import routers
from .views import LabTestTypeViewSet

router = routers.DefaultRouter()
router.register("api/lab_test_type", LabTestTypeViewSet, "lab_test_type")

urlpatterns = router.urls
