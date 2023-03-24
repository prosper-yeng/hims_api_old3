from django.urls import path
from rest_framework import routers
from .views import LabTestBillViewSet

router = routers.DefaultRouter()
router.register("api/lab_test_bill", LabTestBillViewSet, "lab_test_bill")

urlpatterns = router.urls
