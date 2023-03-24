from django.urls import path
from rest_framework import routers
from .views import TransactionLogViewSet, SubmitReadyViewSet

router = routers.DefaultRouter()
router.register("api/transaction_log", TransactionLogViewSet, "transaction_log")
router.register("api/submit_ready", SubmitReadyViewSet, "submit_ready")

urlpatterns = router.urls
