from django.urls import path
from rest_framework import routers
from .views import SponsorTypeViewSet

router = routers.DefaultRouter()
router.register("api/sponsor_type", SponsorTypeViewSet, "sponsor_type")
urlpatterns = router.urls
