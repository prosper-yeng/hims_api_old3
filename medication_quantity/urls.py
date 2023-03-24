from django.urls import path
from rest_framework import routers
from .views import MedicationQuantityViewSet

router = routers.DefaultRouter()
router.register(
    "api/medication_quantity", MedicationQuantityViewSet, "medication_quantity"
)

urlpatterns = router.urls
