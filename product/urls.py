from django.urls import path
from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register("api/product", ProductViewSet, "product")

urlpatterns = router.urls
