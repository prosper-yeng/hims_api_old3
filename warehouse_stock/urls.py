from django.urls import path
from rest_framework import routers
from .views import WarehouseStockViewSet

router = routers.DefaultRouter()
router.register("api/warehouse_stock", WarehouseStockViewSet, "warehouse_stock")

urlpatterns = router.urls
