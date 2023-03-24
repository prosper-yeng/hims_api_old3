from django.urls import path
from rest_framework import routers
from .views import AllergiesViewset, CombinedUserPatientAllergiesView

router = routers.DefaultRouter()
router.register("api/allergies", AllergiesViewset, "allergies")
# urlpatterns = router.urls

urlpatterns = [
    path(
        "api/patient_allergies_list",
        CombinedUserPatientAllergiesView.as_view(),
        name="patient_allergies_list",
    ),
]
urlpatterns += router.urls
