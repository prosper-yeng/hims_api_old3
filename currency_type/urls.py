from django.urls import path
from rest_framework import routers
from .views import CurrencyTypeViewSet

router = routers.DefaultRouter()
router.register("api/currency_type", CurrencyTypeViewSet, "currency_type")

urlpatterns = router.urls
