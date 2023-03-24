from django.urls import path
from rest_framework import routers
from .views import OrderBatchViewSet

router = routers.DefaultRouter()
router.register("api/order_batch", OrderBatchViewSet, "order_batch")

urlpatterns = router.urls
