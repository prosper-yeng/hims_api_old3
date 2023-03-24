# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import PatientSpecificGoalViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/patient-specific-goal", PatientSpecificGoalViewSet, "patient_specific_goal")

urlpatterns = router.urls
