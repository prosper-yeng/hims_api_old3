from django.urls import path
from rest_framework import routers
from .views import RelativeViewset, CombinedUserPatientRelativeView

router = routers.DefaultRouter()
router.register("api/relative", RelativeViewset, "relative")

urlpatterns = [
    path(
        "api/patient_relative_list",
        CombinedUserPatientRelativeView.as_view(),
        name="patient_relative_list",
    ),
]
urlpatterns += router.urls
