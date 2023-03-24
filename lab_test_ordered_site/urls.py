from django.urls import path
from rest_framework import routers
from .views import LabTestOrderedSiteViewSet, CombinedLabTestOrderedSiteView

router = routers.DefaultRouter()
router.register(
    "api/lab_test_ordered_site", LabTestOrderedSiteViewSet, "lab_test_ordered_site"
)

urlpatterns = [
    path(
        "api/lab_test_ordered_site_list",
        CombinedLabTestOrderedSiteView.as_view(),
        name="lab_test_ordered_site_list",
    ),
]
urlpatterns += router.urls
