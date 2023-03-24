from django.urls import path
from rest_framework import routers
from .views import ServiceChargeSponsorViewSet, CombinedServiceChargeSponsorView

router = routers.DefaultRouter()
router.register(
    "api/service_charge_sponsor", ServiceChargeSponsorViewSet, "service_charge_sponsor"
)

# urlpatterns = router.urls
urlpatterns = [
    path(
        "api/service_charge_sponsor_list",
        CombinedServiceChargeSponsorView.as_view(),
        name="service_charge_sponsor_list",
    ),
]
urlpatterns += router.urls
