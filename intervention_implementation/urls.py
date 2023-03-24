# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import InterventionImplementationViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/intervention-implementation", InterventionImplementationViewSet, "intervertion_implementation")

urlpatterns = router.urls
