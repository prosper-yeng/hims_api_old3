from django.urls import path
from rest_framework import routers
from .views import TransactionTypeViewset

router = routers.DefaultRouter()
router.register("api/transaction_type", TransactionTypeViewset, "transaction_type")

urlpatterns = router.urls
