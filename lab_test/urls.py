from django.urls import path
from rest_framework import routers
from .views import LabTestViewSet, CombinedLabTestTypeView

router = routers.DefaultRouter()
router.register("api/lab_test", LabTestViewSet, "lab_test")

urlpatterns = [
    path(
        "api/lab_test_list",
        CombinedLabTestTypeView.as_view(),
        name="lab_test_list",
    ),
]
urlpatterns += router.urls
