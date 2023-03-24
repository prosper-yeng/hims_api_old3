from django.urls import path
from rest_framework import routers
from .views import RelativeTypeViewSet

router = routers.DefaultRouter()
router.register("api/relative_type", RelativeTypeViewSet, "relative_type")

urlpatterns = router.urls
