from django.urls import path
from rest_framework import routers
from .views import ClinicTypeViewSet

router = routers.DefaultRouter()
router.register("api/clinic_type", ClinicTypeViewSet, "clinic_type")

urlpatterns = router.urls
