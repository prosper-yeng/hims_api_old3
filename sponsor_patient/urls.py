from django.urls import path
from rest_framework import routers
from .views import SponsorPatientViewset

router = routers.DefaultRouter()
router.register("api/sponsor_patient", SponsorPatientViewset, "sponsor_patient")

urlpatterns = router.urls
