from django.urls import path
from rest_framework import routers
from .views import DepartmentProductStockUnitViewSet

router = routers.DefaultRouter()
router.register(
    "api/department_product_stock_unit",
    DepartmentProductStockUnitViewSet,
    "department_product_stock_unit",
)

urlpatterns = router.urls
