from django.urls import path
from rest_framework import routers
from .views import PermissionViewSet

router = routers.DefaultRouter()
router = routers.DefaultRouter()
router.register("api/permission", PermissionViewSet, "permission")

urlpatterns = router.urls

# urlpatterns = [
#     path('api/group', GroupView.as_view(), name='group'),
# ]
#
# urlpatterns += router.urls
