from django.urls import path
from rest_framework import routers
from .views import LabTestPriceSponsorViewSet

router = routers.DefaultRouter()
router.register(
    "api/lab_test_price_sponsor", LabTestPriceSponsorViewSet, "lab_test_price_sponsor"
)

urlpatterns = router.urls
