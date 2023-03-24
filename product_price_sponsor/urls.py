from django.urls import path
from rest_framework import routers
from .views import ProductPriceSponsorViewSet

router = routers.DefaultRouter()
router.register(
    "api/product_price_sponsor", ProductPriceSponsorViewSet, "product_price_sponsor"
)

urlpatterns = router.urls
