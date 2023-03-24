from django.urls import path
from rest_framework import routers
from .views import NationViewset

router = routers.DefaultRouter()
router.register("api/nation", NationViewset, "nation")
urlpatterns = router.urls
