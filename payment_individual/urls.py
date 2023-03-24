from django.urls import path
from rest_framework import routers
from .views import PaymentIndividualViewSet, CombinedPaymentIndividualPatientView

router = routers.DefaultRouter()
router.register(
    "api/payment_individual", PaymentIndividualViewSet, "payment_individual"
)

# urlpatterns = router.urls


urlpatterns = [
    path(
        "api/payment_individual_list",
        CombinedPaymentIndividualPatientView.as_view(),
        name="payment_individual_list",
    ),
]
urlpatterns += router.urls
