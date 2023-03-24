# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import InterventionTypeViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/intervention-type", InterventionTypeViewSet, "intervention_type")

urlpatterns = router.urls
