from django.urls import path
from rest_framework import routers
from .views import LabTestSiteViewSet, CombinedLabTestSiteView

router = routers.DefaultRouter()
router.register("api/lab_test_site", LabTestSiteViewSet, "lab_test_site")

urlpatterns = [
    path(
        "api/lab-test-site-list",
        CombinedLabTestSiteView.as_view(),
        name="lab_test_site_list",
    ),
]
urlpatterns += router.urls
