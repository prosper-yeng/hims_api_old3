# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import BedViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/bed", BedViewSet, "bed")

urlpatterns = router.urls
