# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import *

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/patient-needs", PatientNeedsViewSet, "patient_needs")

urlpatterns = router.urls
