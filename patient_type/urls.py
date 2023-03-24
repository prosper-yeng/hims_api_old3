# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import PatientTypeViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/patient_type", PatientTypeViewSet, "patient_type")


urlpatterns = router.urls
