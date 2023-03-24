from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("api/lab_test_order", views.LabTestOrderViewSet, "lab_test_order")
router.register(
    "api/lab_test_order/search",
)

urlpatterns = [
    path(
        "api/lab_test_order/search",
        views.LabTestOrderSearchView.as_view(),
        name="lab_test_order_search",
    ),
]
urlpatterns += router.urls
