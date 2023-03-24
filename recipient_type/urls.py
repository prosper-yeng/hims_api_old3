from django.urls import path
from rest_framework import routers
from .views import RecipientTypeViewSet

router = routers.DefaultRouter()
router.register("api/recipient_type", RecipientTypeViewSet, "recipient_type")

urlpatterns = router.urls
