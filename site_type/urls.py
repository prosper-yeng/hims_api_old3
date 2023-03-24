from django.urls import path
from rest_framework import routers
from .views import SiteTypeViewSet

router = routers.DefaultRouter()
router.register("api/site_type", SiteTypeViewSet, "site_type")

urlpatterns = router.urls
