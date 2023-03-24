from django.urls import path
from rest_framework import routers
from .views import MedicationOrderViewSet

router = routers.DefaultRouter()
router.register("api/medication_order", MedicationOrderViewSet, "medication_order")

urlpatterns = router.urls
