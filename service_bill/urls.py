from django.urls import path
from rest_framework import routers
from .views import ServiceBillViewSet

router = routers.DefaultRouter()
router.register("api/service_bill", ServiceBillViewSet, "service_bill")

urlpatterns = router.urls
