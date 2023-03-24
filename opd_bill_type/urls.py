from django.urls import path
from rest_framework import routers
from .views import OpdBillTypeViewSet

router = routers.DefaultRouter()
router.register("api/opd_bill_type", OpdBillTypeViewSet, "opd_bill_type")

urlpatterns = router.urls
