from django.urls import path
from rest_framework import routers
from .views import ConsultingRoomViewSet

router = routers.DefaultRouter()
router.register("api/consulting_room", ConsultingRoomViewSet, "consulting_room")

urlpatterns = router.urls
