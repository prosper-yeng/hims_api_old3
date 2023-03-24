from django.urls import path
from rest_framework import routers
from .views import StoreViewSet

router = routers.DefaultRouter()
router.register("api/store", StoreViewSet, "store")

urlpatterns = router.urls
