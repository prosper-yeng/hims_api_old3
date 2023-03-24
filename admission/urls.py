# Python/django imports
from django.urls import path
from rest_framework.routers import DefaultRouter

# Local apps imports
from .views import *

router = DefaultRouter()

# Admin routes
router.register("api/admission", AdmissionViewSet)
#urlpatterns = router.urls

urlpatterns = [
    path(
        "api/admission/search",
        AdmissionSearchView.as_view(),
        name="admission_read",
    )
]

urlpatterns += router.urls
