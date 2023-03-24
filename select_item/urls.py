from django.urls import path
from rest_framework import routers
from .views import SelectItemViewset

router = routers.DefaultRouter()
router.register("api/select_item", SelectItemViewset, "select_item")

urlpatterns = router.urls
