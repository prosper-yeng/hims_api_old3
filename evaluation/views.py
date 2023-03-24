from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Evaluation
from .serializers import EvaluationSerializer, EvaluationDetailsSerializer


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = [IsAuthenticated]
    action_serializers = {
        "retrieve": EvaluationDetailsSerializer,
        "list": EvaluationDetailsSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(EvaluationViewSet, self).get_serializer_class()
