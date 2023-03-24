from django.urls import path
from rest_framework import routers

from .serializers import CombinedPaymentDetailSerializer
from .views import PaymentDetailIndividualViewSet, CombinedPaymentDetailView

router = routers.DefaultRouter()
router.register(
    "api/payment_detail_by_individual",
    PaymentDetailIndividualViewSet,
    "payment_detail_by_individual",
)

# urlpatterns = router.urls

urlpatterns = [
    path(
        "api/payment_detail_by_individual_list",
        CombinedPaymentDetailView.as_view(),
        name="payment_detail_by_individual_list",
    ),
]
urlpatterns += router.urls
