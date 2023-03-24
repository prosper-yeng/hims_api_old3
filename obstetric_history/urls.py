# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import *

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/obstetric-history", ObstetricHistoryViewSet, "obstetric_history")

urlpatterns = [
    path(
        "api/patient_obstetric_history_list",
        CombinedUserPatientObstetricHistoryView.as_view(),
        name="patient_obstetric_history_list",
    ),
]
urlpatterns += router.urls
