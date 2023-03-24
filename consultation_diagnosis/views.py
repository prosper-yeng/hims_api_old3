# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    ConsultationDiagnosisSerializer,
    CombinedConsultedDiagnosedPatientSerializer,
)
from .models import Consultation, ConsultationDiagnosis
from rest_framework.response import Response
from rest_framework.views import APIView


class ConsultationDiagnosisViewSet(viewsets.ModelViewSet):
    queryset = ConsultationDiagnosis.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ConsultationDiagnosisSerializer


class ConsultationDiagnosisDetailViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]
    serializer_class = ConsultationDiagnosisSerializer

    def get_queryset(self):
        trans_id = self.request.query_params.get("trans_id", None)
        queryset = ConsultationDiagnosis.objects.filter(transaction_id=trans_id)

        return queryset


class CombinedConsultedDiagnosedPatientView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = ConsultationDiagnosis.objects.all()
        serialized = CombinedConsultedDiagnosedPatientSerializer(query_data, many=True)
        return Response(serialized.data)
