from django.urls import path
from rest_framework import routers
from .views import DiagnosedProcedureViewSet, CombinedDiagnosedProcedureView

router = routers.DefaultRouter()
router.register(
    "api/diagnosed_procedure", DiagnosedProcedureViewSet, "diagnosed_procedure"
)
# router.register ( 'api/diagnosed_procedure_detail', DiagnosedProcedureDetailViewSet, 'diagnosed_procedure_detail' )
# urlpatterns = router.urls

urlpatterns = [
    path(
        "api/diagnosis_procedure_list",
        CombinedDiagnosedProcedureView.as_view(),
        name="diagnosis_procedure_list",
    ),
]
urlpatterns += router.urls
