from django.urls import path
from rest_framework import routers
from .views import BuyerViewSet

router = routers.DefaultRouter()
router.register("api/buyer", BuyerViewSet, "buyer")

urlpatterns = router.urls
