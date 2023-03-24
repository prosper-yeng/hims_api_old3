# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import HabitViewSet, CombinedUserPatientHabitView

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/habit", HabitViewSet, "habit")

urlpatterns = [
    path(
        "api/patient_habit_list",
        CombinedUserPatientHabitView.as_view(),
        name="patient_habit_list",
    ),
]
urlpatterns += router.urls