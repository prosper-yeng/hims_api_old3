from django.urls import path
from rest_framework import routers
from .views import ServiceTypeViewSet

router = routers.DefaultRouter()
router.register("api/service_type", ServiceTypeViewSet, "service_type")

urlpatterns = router.urls
