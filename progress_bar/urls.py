from django.urls import path
from rest_framework import routers
from .views import ProgressBarViewSet

router = routers.DefaultRouter()
router.register("api/progress_bar", ProgressBarViewSet, "progress_bar")
urlpatterns = router.urls
