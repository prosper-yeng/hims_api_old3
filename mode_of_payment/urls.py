from django.urls import path
from rest_framework import routers
from .views import ModeOfPaymentViewSet

router = routers.DefaultRouter()
router.register("api/mode_of_payment", ModeOfPaymentViewSet, "mode_of_payment")

urlpatterns = router.urls
