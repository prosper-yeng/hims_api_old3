from django.urls import path
from rest_framework import routers
from .views import FacilityViewset, CombinedFaciltyTownView

router = routers.DefaultRouter()
router.register("api/facility", FacilityViewset, "facility")

# urlpatterns = router.urls

urlpatterns = [
    path(
        "api/facility_town_list",
        CombinedFaciltyTownView.as_view(),
        name="facility_town_list",
    ),
]
urlpatterns += router.urls
