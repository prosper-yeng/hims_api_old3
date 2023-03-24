from django.urls import path
from rest_framework import routers
from .views import AddressViewset

router = routers.DefaultRouter()
router.register("api/address", AddressViewset, "address")

urlpatterns = router.urls
