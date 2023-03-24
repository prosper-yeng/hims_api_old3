from django.urls import path
from rest_framework import routers
from .views import LabTestPriceViewSet

router = routers.DefaultRouter()
router.register("api/lab_test_price", LabTestPriceViewSet, "lab_test_price")

urlpatterns = router.urls
