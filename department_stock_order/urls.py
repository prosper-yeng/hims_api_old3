from django.urls import path
from rest_framework import routers
from .views import DepartmentStockOrderViewSet, CombinedLDepartmentStockView

router = routers.DefaultRouter()
router.register(
    "api/department_stock_order", DepartmentStockOrderViewSet, "department_stock_order"
)
urlpatterns = [
    path(
        "api/department_stock_order_list",
        CombinedLDepartmentStockView.as_view(),
        name="department_stock_order_list",
    ),
]

urlpatterns += router.urls
