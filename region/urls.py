from django.urls import path
from rest_framework import routers
from .views import RegionViewset, CombinedRegionNationView

router = routers.DefaultRouter()
router.register("api/region", RegionViewset, "region")
# urlpatterns = router.urls


urlpatterns = [
    path(
        "api/region_nation_list",
        CombinedRegionNationView.as_view(),
        name="region_nation_list",
    ),
]
urlpatterns += router.urls
