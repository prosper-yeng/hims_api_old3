from django.urls import path
from rest_framework import routers
from .views import WarehouseViewSet

router = routers.DefaultRouter()
router.register("api/warehouse", WarehouseViewSet, "warehouse")

urlpatterns = router.urls
