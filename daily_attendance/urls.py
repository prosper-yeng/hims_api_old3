from django.urls import path
from rest_framework import routers
from .views import DailyAttendanceViewset, CombinedPatientAttendanceView

router = routers.DefaultRouter()
router.register("api/attendance", DailyAttendanceViewset, "attendance")
urlpatterns = [
    path(
        "api/patient_attendance_list",
        CombinedPatientAttendanceView.as_view(),
        name="patient_attendance_list",
    ),
]
urlpatterns += router.urls
