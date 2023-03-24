from django.urls import path
from rest_framework import routers
from .views import MedicationPriceViewSet

router = routers.DefaultRouter()
router.register("api/medication_price", MedicationPriceViewSet, "medication_price")

urlpatterns = router.urls
