from django.urls import path
from rest_framework import routers
from .views import DistrictViewset, CombinedDistrictRegionView

router = routers.DefaultRouter()
router.register("api/district", DistrictViewset, "district")
# urlpatterns = router.urls


urlpatterns = [
    path(
        "api/district_region_list",
        CombinedDistrictRegionView.as_view(),
        name="district_region_list",
    ),
]
urlpatterns += router.urls
