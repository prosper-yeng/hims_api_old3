# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import WardViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/ward", WardViewSet, "ward")

urlpatterns = router.urls
