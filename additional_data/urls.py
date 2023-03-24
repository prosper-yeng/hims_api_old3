# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import AdditionalDataViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/additional-data", AdditionalDataViewSet, "additional_data")

urlpatterns = router.urls
