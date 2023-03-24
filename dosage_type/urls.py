from django.urls import path
from rest_framework import routers
from .views import DosageTypeViewSet

router = routers.DefaultRouter()
router.register("api/dosage_type", DosageTypeViewSet, "dosage_type")

urlpatterns = router.urls
