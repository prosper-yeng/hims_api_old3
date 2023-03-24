from django.urls import path
from rest_framework import routers
from .views import ProductPriceViewSet

router = routers.DefaultRouter()
router.register("api/product_price", ProductPriceViewSet, "product_price")

urlpatterns = router.urls
