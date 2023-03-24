from django.urls import path
from rest_framework import routers
from .views import ServiceChargeViewSet, CombinedServiceChargeView

router = routers.DefaultRouter()
router.register("api/service_charge", ServiceChargeViewSet, "service_charge")

# urlpatterns = router.urls
urlpatterns = [
    path(
        "api/service_charge_list",
        CombinedServiceChargeView.as_view(),
        name="service_charge_list",
    ),
]
urlpatterns += router.urls
