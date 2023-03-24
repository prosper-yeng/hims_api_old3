# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import TreatmentPlanViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/treatment_plan", TreatmentPlanViewSet, "treatment_plan")

urlpatterns = router.urls
