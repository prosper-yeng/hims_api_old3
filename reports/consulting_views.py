from rest_framework import generics

# from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from medication.models import Medication
from medication.serializers import MedicationDetailSerializer

from consultation.models import Consultation
from consultation.serializers import CombinedConsultationVitalSignSerializer

from diagnosis.models import Diagnosis
from diagnosis.serializers import DiagnosisDetailSerializer


class DiagnosisHistoryViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DiagnosisDetailSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = Diagnosis.objects.all()

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)


class ConsultationHistoryViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CombinedConsultationVitalSignSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = Consultation.objects.all()

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)


class PatientsMedicalHistoryViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MedicationDetailSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = Medication.objects.all().select_related(
            "patient", "attendance", "sponsor", "prescription", "product", "status"
        )

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)
