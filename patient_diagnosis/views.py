from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import PatientDiagnosis
from .serializers import PatientDiagnosisSerializer, PatientDiagnosisDetailsSerializer


class PatientDiagnosisViewSet(viewsets.ModelViewSet):
    queryset = PatientDiagnosis.objects.all()
    serializer_class = PatientDiagnosisSerializer
    permission_classes = [IsAuthenticated]
    action_serializers = {
        "retrieve": PatientDiagnosisDetailsSerializer,
        "list": PatientDiagnosisDetailsSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(PatientDiagnosisViewSet, self).get_serializer_class()
