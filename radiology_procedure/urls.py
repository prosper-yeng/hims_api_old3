# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import RadiologyProcedureViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register(
    "api/radiology_procedure", RadiologyProcedureViewSet, "radiology_procedure"
)

urlpatterns = router.urls
