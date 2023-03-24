from django.urls import path
from rest_framework import routers
from .views import PaymentDetailViewSet

router = routers.DefaultRouter()
router.register("api/payment_detail", PaymentDetailViewSet, "payment_detail")

urlpatterns = router.urls
