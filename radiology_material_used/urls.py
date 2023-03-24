# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import RadiologyMaterialUsedViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register(
    "api/radiology_material_used",
    RadiologyMaterialUsedViewSet,
    "radiology_material_used",
)

urlpatterns = router.urls
