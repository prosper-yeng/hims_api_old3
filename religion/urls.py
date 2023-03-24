from django.urls import path
from rest_framework import routers
from .views import ReligionViewset

router = routers.DefaultRouter()
router.register("api/religion", ReligionViewset, "religion")
urlpatterns = router.urls
