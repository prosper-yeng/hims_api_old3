from django.urls import path
from rest_framework import routers


from .views import CombinedPaymentDetailView, PaymentDetailBySponsorViewSet

router = routers.DefaultRouter()
router.register(
    "api/payment_detail_by_sponsor",
    PaymentDetailBySponsorViewSet,
    "payment_detail_by_sponsor",
)

# urlpatterns = router.urls

urlpatterns = [
    path(
        "api/payment_detail_by_sponsore_list",
        CombinedPaymentDetailView.as_view(),
        name="payment_detail_by_sponsore_list",
    ),
]
urlpatterns += router.urls
