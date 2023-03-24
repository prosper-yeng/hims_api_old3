# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import PhysicalExaminationViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/physical-examination", PhysicalExaminationViewSet, "physical_examination")

urlpatterns = router.urls
