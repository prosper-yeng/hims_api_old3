from django.urls import path
from rest_framework import routers
from .views import RecommendedDosageViewSet

router = routers.DefaultRouter()
router.register(
    "api/recommended_dosage", RecommendedDosageViewSet, "recommended_dosage"
)

urlpatterns = router.urls
