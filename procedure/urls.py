from django.urls import path
from rest_framework import routers
from .views import ProcedureViewSet

router = routers.DefaultRouter()
router.register("api/procedure", ProcedureViewSet, "procedure")

urlpatterns = router.urls
