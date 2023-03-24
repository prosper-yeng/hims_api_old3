from django.urls import path
from rest_framework import routers
from .views import ClientViewSet

router = routers.DefaultRouter()
router.register("api/client", ClientViewSet, "client")

urlpatterns = router.urls
