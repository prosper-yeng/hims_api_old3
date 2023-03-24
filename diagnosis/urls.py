from django.urls import path
from rest_framework import routers
from .views import DiagnosisViewSet

router = routers.DefaultRouter()
router.register("api/diagnosis", DiagnosisViewSet, "diagnosis")

urlpatterns = router.urls
