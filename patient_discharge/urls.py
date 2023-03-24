# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import PatientDischargeViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/patient_discharge", PatientDischargeViewSet, "patient_discharge")

urlpatterns = router.urls
