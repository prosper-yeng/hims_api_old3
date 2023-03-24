from django.urls import path
from rest_framework import routers
from .views import AttendanceTypeViewSet

router = routers.DefaultRouter()
router.register("api/attendance_type", AttendanceTypeViewSet, "attendance_type")
urlpatterns = router.urls
