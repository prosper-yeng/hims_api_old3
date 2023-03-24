from django.urls import path
from rest_framework import routers
from .views import OccupationViewset

router = routers.DefaultRouter()
router.register("api/occupation", OccupationViewset, "occupation")
urlpatterns = router.urls
