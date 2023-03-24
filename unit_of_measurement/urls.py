from django.urls import path
from rest_framework import routers
from .views import UnitOfMeasurementViewSet

router = routers.DefaultRouter()
router.register(
    "api/unit_of_measurement", UnitOfMeasurementViewSet, "unit_of_measurement"
)

urlpatterns = router.urls
