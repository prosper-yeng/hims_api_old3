from django.urls import path
from rest_framework import routers
from .views import MedicationBillViewSet

router = routers.DefaultRouter()
router.register("api/medication_bill", MedicationBillViewSet, "medication_bill")

urlpatterns = router.urls
