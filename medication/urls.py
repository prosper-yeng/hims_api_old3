from django.urls import path
from rest_framework import routers
from .views import MedicationViewSet

router = routers.DefaultRouter()
router.register("api/medication", MedicationViewSet, "medication")

urlpatterns = router.urls
