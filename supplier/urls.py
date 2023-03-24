from django.urls import path
from rest_framework import routers
from .views import SupplierViewSet

router = routers.DefaultRouter()
router.register("api/supplier", SupplierViewSet, "supplier")

urlpatterns = router.urls
