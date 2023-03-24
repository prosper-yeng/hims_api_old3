# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import RadiologyProcedurePriceViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register(
    "api/radiology_procedure_price",
    RadiologyProcedurePriceViewSet,
    "radiology_procedure_price",
)

urlpatterns = router.urls
