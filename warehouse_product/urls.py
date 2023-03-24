from django.urls import path
from rest_framework import routers
from .views import WarehouseProductViewSet, CombinedWarehouseProductView

router = routers.DefaultRouter()
router.register("api/warehouse_product", WarehouseProductViewSet, "warehouse_product")

# urlpatterns = router.urls


urlpatterns = [
    path(
        "api/warehous_product_list",
        CombinedWarehouseProductView.as_view(),
        name="warehous_product_list",
    ),
]
urlpatterns += router.urls
