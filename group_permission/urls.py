from rest_framework import routers
from .views import GroupPermissionViewSet

router = routers.DefaultRouter()
router.register("api/group_permission", GroupPermissionViewSet, "group_permission")

urlpatterns = router.urls
