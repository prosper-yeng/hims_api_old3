from django.urls import path
from rest_framework import routers
from .views import ServiceViewSet, CombinedServiceTypeServiceView

router = routers.DefaultRouter()
router.register("api/service", ServiceViewSet, "service")
# router.register('api/service_type_service_list', CombinedServiceTypeServiceView, 'service_type_service_list')
# router.register('api/registration_service', RegistrationServiceViewSet, 'registration_service')

# urlpatterns = router.urls


urlpatterns = [
    path(
        "api/service_type_service_list",
        CombinedServiceTypeServiceView.as_view(),
        name="service_type_service_list",
    ),
]
urlpatterns += router.urls
