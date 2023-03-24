from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import TreatmentPlan
from .serializers import TreatmentPlanSerializer, TreatmentPlanDetailsSerializer


class TreatmentPlanViewSet(viewsets.ModelViewSet):
    queryset = TreatmentPlan.objects.all()
    serializer_class = TreatmentPlanSerializer
    permission_classes = [IsAuthenticated]
    action_serializers = {
        "retrieve": TreatmentPlanDetailsSerializer,
        "list": TreatmentPlanDetailsSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(TreatmentPlanViewSet, self).get_serializer_class()
