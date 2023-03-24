from django.urls import path
from rest_framework import routers
from .views import TestConsumableViewSet

router = routers.DefaultRouter()
router.register("api/test_consumable", TestConsumableViewSet, "test_consumable")

urlpatterns = router.urls
