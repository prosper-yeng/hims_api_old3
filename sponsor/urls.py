from django.urls import path
from rest_framework import routers
from .views import SponsorViewSet

router = routers.DefaultRouter()
router.register("api/sponsor", SponsorViewSet, "sponsor")

urlpatterns = router.urls
