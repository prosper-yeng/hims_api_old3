# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import EvaluationViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/evaluation", EvaluationViewSet, "evaluation")

urlpatterns = router.urls
