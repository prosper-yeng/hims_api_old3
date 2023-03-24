from django.urls import path
from rest_framework import routers
from .views import ClientTypeViewSet

router = routers.DefaultRouter()
router.register("api/client_type", ClientTypeViewSet, "client_type")

urlpatterns = router.urls
