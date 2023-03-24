from django.urls import path
from rest_framework import routers
from .views import SelectUnitViewset

router = routers.DefaultRouter()
router.register("api/select_unit", SelectUnitViewset, "select_unit")

urlpatterns = router.urls
