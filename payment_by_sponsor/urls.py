from django.urls import path
from rest_framework import routers
from .views import PaymentBySponsorViewSet, CombinedPaymentSponsorView

router = routers.DefaultRouter()
router.register("api/payment_by_sponsor", PaymentBySponsorViewSet, "payment_by_sponsor")

# urlpatterns = router.urls


urlpatterns = [
    path(
        "api/payment_by_sponsor_list",
        CombinedPaymentSponsorView.as_view(),
        name="payment_by_sponsor_list",
    ),
]
urlpatterns += router.urls
