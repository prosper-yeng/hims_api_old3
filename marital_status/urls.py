from django.urls import path
from rest_framework import routers
from .views import MaritalStatusViewset

router = routers.DefaultRouter()
router.register("api/marital_status", MaritalStatusViewset, "marital_status")
urlpatterns = router.urls
