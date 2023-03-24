from django.urls import path
from rest_framework import routers
from .views import ProductCategoryViewSet

router = routers.DefaultRouter()
router.register("api/product_category", ProductCategoryViewSet, "product_category")

urlpatterns = router.urls
