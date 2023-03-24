# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import RadiologyProcedurePriceSponsorViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register(
    "api/radiology_procedure_price_sponsor",
    RadiologyProcedurePriceSponsorViewSet,
    "radiology_procedure_price_sponsor",
)

urlpatterns = router.urls
