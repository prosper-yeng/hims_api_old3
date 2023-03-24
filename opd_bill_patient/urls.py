from django.urls import path
from rest_framework import routers
from .views import OpdBillPatientViewSet

router = routers.DefaultRouter()
router.register("api/opd_bill_patient", OpdBillPatientViewSet, "opd_bill_patient")

urlpatterns = router.urls
