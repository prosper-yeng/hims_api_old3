from django.urls import path
from rest_framework import routers
from .views import StatusViewset

router = routers.DefaultRouter()
router.register("api/status", StatusViewset, "status")
urlpatterns = router.urls
