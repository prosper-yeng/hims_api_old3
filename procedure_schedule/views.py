# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    ProcedureChargeBySponsorSerializer,
    ProcedureScheduleSerializer,
    CombinedProcedureScheduleSerializer,
)
from .models import ProcedureChargeBySponsor, ProcedureSchedule


class ProcedureScheduleViewSet(viewsets.ModelViewSet):
    queryset = ProcedureSchedule.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProcedureScheduleSerializer


class CombinedProcedureScheduleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = ProcedureSchedule.objects.all()
        serialized = CombinedProcedureScheduleSerializer(query_data, many=True)
        return Response(serialized.data)
