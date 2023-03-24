from django.urls import path
from rest_framework import routers
from .views import TransactionViewSet, MyTasksViewSet, TransactionSubmitViewSet

router = routers.DefaultRouter()
router.register("api/transaction", TransactionViewSet, "transaction")
router.register(
    "api/transaction_submit", TransactionSubmitViewSet, "transaction_submit"
)
router.register("api/my_tasks", MyTasksViewSet, "my_tasks")

urlpatterns = router.urls
