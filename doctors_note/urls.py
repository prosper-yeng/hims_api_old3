# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import DoctorsNoteViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register("api/doctors_note", DoctorsNoteViewSet, "doctors_note")

urlpatterns = router.urls
