from django.urls import path
from rest_framework import routers
from .views import LanguageViewset

router = routers.DefaultRouter()
router.register("api/language", LanguageViewset, "language")
urlpatterns = router.urls
