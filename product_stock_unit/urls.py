from django.urls import path
from rest_framework import routers
from .views import ProductStockUnitViewSet

router = routers.DefaultRouter()
router.register("api/product_stock_unit", ProductStockUnitViewSet, "product_stock_unit")

urlpatterns = router.urls
