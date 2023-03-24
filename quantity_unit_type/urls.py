from django.urls import path
from rest_framework import routers
from .views import MedicationTypeViewSet

router = routers.DefaultRouter()
router.register("api/quantity_unit_type", MedicationTypeViewSet, "quantity_unit_type")

urlpatterns = router.urls
