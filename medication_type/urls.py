from django.urls import path
from rest_framework import routers
from .views import MedicationTypeViewSet

router = routers.DefaultRouter()
router.register("api/medication_type", MedicationTypeViewSet, "medication_type")

urlpatterns = router.urls
