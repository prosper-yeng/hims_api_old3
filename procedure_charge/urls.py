from django.urls import path
from rest_framework import routers
from .views import ProcedureChargeViewSet, CombinedProcedureChargeView

router = routers.DefaultRouter()
router.register("api/procedure_charge", ProcedureChargeViewSet, "procedure_charge")

# urlpatterns = router.urls
urlpatterns = [
    path(
        "api/procedure_charge_list",
        CombinedProcedureChargeView.as_view(),
        name="procedure_charge_list",
    ),
]
urlpatterns += router.urls
