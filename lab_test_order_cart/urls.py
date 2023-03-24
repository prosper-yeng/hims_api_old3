from django.urls import path
from rest_framework import routers
from .views import LabTestOrderCartViewSet

router = routers.DefaultRouter()
router.register(
    "api/lab_test_order_cart", LabTestOrderCartViewSet, "lab_test_order_cart"
)

urlpatterns = router.urls
