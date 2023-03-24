from django.urls import path
from rest_framework import routers
from .views import LabTestOrderedSampleViewSet, CombinedLabTestOrderedSampleView

router = routers.DefaultRouter()
router.register(
    "api/lab_test_ordered_sample",
    LabTestOrderedSampleViewSet,
    "lab_test_ordered_sample",
)

urlpatterns = [
    path(
        "api/lab_test_ordered_sample_list",
        CombinedLabTestOrderedSampleView.as_view(),
        name="lab_test_ordered_sample_list",
    ),
]

urlpatterns += router.urls
