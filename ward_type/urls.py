# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import WardTypeViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/ward_type", WardTypeViewSet, "ward_type")

urlpatterns = router.urls
