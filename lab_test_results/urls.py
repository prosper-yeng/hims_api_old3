from django.urls import path
from rest_framework import routers
from .views import LabTestResultsViewSet, CombinedLabTestOrderResultView

router = routers.DefaultRouter()
router.register("api/lab_test_results", LabTestResultsViewSet, "lab_test_results")

# urlpatterns = router.urls
urlpatterns = [
    path(
        "api/lab_test_result_list",
        CombinedLabTestOrderResultView.as_view(),
        name="lab_test_result_list",
    ),
]
urlpatterns += router.urls
