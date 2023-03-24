from django.urls import path
from rest_framework import routers
from .views import ProcedureChargeBySponsorViewSet, CombinedProcedureChargeBySponsorView

router = routers.DefaultRouter()
router.register(
    "api/procedure_charge_by_sponsor",
    ProcedureChargeBySponsorViewSet,
    "procedure_charge_by_sponsor",
)

# urlpatterns = router.urls
urlpatterns = [
    path(
        "api/procedure_charge_by_sponsor_list",
        CombinedProcedureChargeBySponsorView.as_view(),
        name="procedure_charge_by_sponsor_list",
    ),
]
urlpatterns += router.urls
