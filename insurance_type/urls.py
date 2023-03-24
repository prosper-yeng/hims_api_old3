from django.urls import path
from rest_framework import routers
from .views import InsuranceTypeViewSet

router = routers.DefaultRouter()
router.register("api/insurance_type", InsuranceTypeViewSet, "insurance_type")

urlpatterns = router.urls
