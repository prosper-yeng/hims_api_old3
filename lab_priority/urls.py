from django.urls import path
from rest_framework import routers
from .views import LabPriorityViewset

router = routers.DefaultRouter()
router.register("api/lab_priority", LabPriorityViewset, "lab_priority")
urlpatterns = router.urls
