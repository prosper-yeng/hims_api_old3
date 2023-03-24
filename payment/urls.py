from django.urls import path
from rest_framework import routers
from .views import PaymentViewSet, CombinedPaymentPatientUserView

router = routers.DefaultRouter()
router.register("api/payment", PaymentViewSet, "payment")

# urlpatterns = router.urls


urlpatterns = [
    path(
        "api/patient_payment_list",
        CombinedPaymentPatientUserView.as_view(),
        name="patient_payment_list",
    ),
]
urlpatterns += router.urls
