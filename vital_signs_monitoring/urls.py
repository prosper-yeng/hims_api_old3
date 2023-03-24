# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import VitalSignsMonitoringViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register(
    "api/vital_signs_monitoring", VitalSignsMonitoringViewSet, "vital_signs_monitoring"
)

urlpatterns = router.urls
