from django.urls import path
from rest_framework import routers
from .views import TownViewset, CombinedTownDistrictView

router = routers.DefaultRouter()
router.register("api/town", TownViewset, "town")
# urlpatterns = router.urls


urlpatterns = [
    path(
        "api/town_district_list",
        CombinedTownDistrictView.as_view(),
        name="town_district_list",
    ),
]
urlpatterns += router.urls
