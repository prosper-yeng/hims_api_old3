from django.urls import path
from rest_framework import routers
from .views import WorkFlowViewSet, WorkFlowAccessLevelViewSet

router = routers.DefaultRouter()
router.register("api/workflow", WorkFlowViewSet, "work_flow")
router.register("api/access_level", WorkFlowAccessLevelViewSet, "access_level")

urlpatterns = router.urls
