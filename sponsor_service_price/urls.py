from django.urls import path
from rest_framework import routers
from .views import SponsorServicePriceViewset

router = routers.DefaultRouter()
router.register(
    "api/sponsor_service_price", SponsorServicePriceViewset, "sponsor_service_price"
)
urlpatterns = router.urls
