from django.urls import path
from rest_framework import routers
from .views import (
    ProductTypeViewSet,
    CombinedProductCategoryTypeView,
    GetProductCategoryByCategoryTypeView,
)

router = routers.DefaultRouter()
router.register("api/product_type", ProductTypeViewSet, "product_type")
# urlpatterns = router.urls

urlpatterns = [
    path(
        "api/product_category_type_list",
        CombinedProductCategoryTypeView.as_view(),
        name="product_category_type_list",
    ),
    path(
        "api/product_category_by_category",
        GetProductCategoryByCategoryTypeView.as_view(),
        name="product_category_by_category",
    ),
]
urlpatterns += router.urls
