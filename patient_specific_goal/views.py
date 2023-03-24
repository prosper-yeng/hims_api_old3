from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import PatientSpecificGoal
from .serializers import PatientSpecificGoalSerializer, PatientSpecificGoalDetailsSerializer


class PatientSpecificGoalViewSet(viewsets.ModelViewSet):
    queryset = PatientSpecificGoal.objects.all()
    serializer_class = PatientSpecificGoalSerializer
    permission_classes = [IsAuthenticated]
    action_serializers = {
        "retrieve": PatientSpecificGoalDetailsSerializer,
        "list": PatientSpecificGoalDetailsSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(PatientSpecificGoalViewSet, self).get_serializer_class()
