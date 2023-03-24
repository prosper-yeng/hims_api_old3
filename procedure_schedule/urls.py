from django.urls import path
from rest_framework import routers
from .views import ProcedureScheduleViewSet, CombinedProcedureScheduleView

router = routers.DefaultRouter()
router.register(
    "api/procedure_schedule", ProcedureScheduleViewSet, "procedure_schedule"
)

# urlpatterns = router.urls
urlpatterns = [
    path(
        "api/procedure_schedule_list",
        CombinedProcedureScheduleView.as_view(),
        name="procedure_schedule_list",
    ),
]
urlpatterns += router.urls
