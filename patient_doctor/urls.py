from rest_framework import routers
from .views import PatientDoctorViewSet

router = routers.DefaultRouter()
router.register("api/patient_doctor", PatientDoctorViewSet, "patient_doctor")

urlpatterns = router.urls
