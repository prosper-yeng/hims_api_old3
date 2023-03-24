# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PatientServiceCharge
from .serializers import (
    PatientServiceChargeSerializer,
    CombinedPatientServiceChargeSerializer,
)


class PatientServiceChargeViewSet(viewsets.ModelViewSet):
    queryset = PatientServiceCharge.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PatientServiceChargeSerializer


class CombinedPatientServiceChargeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = PatientServiceCharge.objects.all()
        serialized = CombinedPatientServiceChargeSerializer(query_data, many=True)
        return Response(serialized.data)
