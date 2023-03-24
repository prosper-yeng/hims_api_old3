# Python/django imports
from django.urls import path
from rest_framework import routers

# Local apps imports
from .views import RadiologyCategoryViewSet

# Declare router
router = routers.DefaultRouter()

# Declaring general routes
router.register(
    "api/radiology_category", RadiologyCategoryViewSet, "radiology_category"
)

urlpatterns = router.urls
