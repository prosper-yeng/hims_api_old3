from django.urls import path
from rest_framework import routers
from .views import PersonTitleViewset

router = routers.DefaultRouter()
router.register("api/person_title", PersonTitleViewset, "person_title")
urlpatterns = router.urls
