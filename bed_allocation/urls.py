# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import *

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/bed_allocation", BedAllocationViewSet, "bed_allocation")

urlpatterns = router.urls
