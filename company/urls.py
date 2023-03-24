from django.urls import path
from rest_framework import routers
from .views import CompanyViewSet

router = routers.DefaultRouter()
router.register("api/company", CompanyViewSet, "company")

urlpatterns = router.urls
