# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import PsychosocialHistoryViewSet, CombinedUserPatientPsychosocialHistoryView

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/psychosocial_history", PsychosocialHistoryViewSet, "psychosocial_history")

urlpatterns = [
    path(
        "api/patient_psychosocial_history_list",
        CombinedUserPatientPsychosocialHistoryView.as_view(),
        name="patient_psychosocial_history_list",
    ),
]
urlpatterns += router.urls
