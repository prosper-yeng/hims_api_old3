from django.urls import path
from rest_framework import routers
from .views import SampleTypeViewset

router = routers.DefaultRouter()
router.register("api/sample_type", SampleTypeViewset, "sample_type")
urlpatterns = router.urls
