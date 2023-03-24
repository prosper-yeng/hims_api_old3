from django.urls import path
from rest_framework import routers
from .views import MedicationBillDetailViewSet

router = routers.DefaultRouter()
router.register(
    "api/medication_bill_detail", MedicationBillDetailViewSet, "medication_bill_detail"
)

urlpatterns = router.urls
