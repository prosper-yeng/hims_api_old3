from django.urls import path
from rest_framework import routers
from .views import MedicationQuantityUnitViewSet

router = routers.DefaultRouter()
router.register(
    "api/medication_quantity_unit",
    MedicationQuantityUnitViewSet,
    "medication_quantity_unit",
)

urlpatterns = router.urls
