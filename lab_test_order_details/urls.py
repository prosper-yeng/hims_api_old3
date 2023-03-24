from django.urls import path
from rest_framework import routers
from .views import (
    LabTestOrderDetailsViewSet,
    CombinedLabTestOrderDetailView,
    LabTestOrderDetailsSearchView,
)

router = routers.DefaultRouter()
router.register(
    "api/lab_test_order_details", LabTestOrderDetailsViewSet, "lab_test_order_details"
)

urlpatterns = [
    path(
        "api/lab_test_order_detail_list",
        CombinedLabTestOrderDetailView.as_view(),
        name="lab_test_order_detail_list",
    ),
    path(
        "api/lab_test_order_details_search",
        LabTestOrderDetailsSearchView.as_view(),
        name="lab_test_order_details_search",
    ),
]

urlpatterns += router.urls
