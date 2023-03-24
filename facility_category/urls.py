from django.urls import path
from rest_framework import routers
from .views import FacilityCategoryViewset

router = routers.DefaultRouter()
router.register("api/facility_category", FacilityCategoryViewset, "facility_category")
urlpatterns = router.urls
