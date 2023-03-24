# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import RadiologyProcedureResultViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register(
    "api/radiology_procedure_result",
    RadiologyProcedureResultViewSet,
    "radiology_procedure_result",
)

urlpatterns = router.urls
