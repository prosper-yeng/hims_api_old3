# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import ProcedureCareViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/procedure_care", ProcedureCareViewSet, "procedure_care")

urlpatterns = router.urls
