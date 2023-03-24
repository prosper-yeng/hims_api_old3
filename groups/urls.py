from rest_framework import routers
from django.urls import path
from .views import (
    GroupDetails,
    GroupViewSet,
    UpdateGroup,
    UpdateGroupStatus,
    CombinedGroupPermissionView,
)

router = routers.DefaultRouter()
router.register("api/group", GroupViewSet, "group")

# urlpatterns = router.urls

urlpatterns = [
    path(
        "api/group_permission_list",
        CombinedGroupPermissionView.as_view(),
        name="group_permission_list",
    ),
]

urlpatterns += router.urls
