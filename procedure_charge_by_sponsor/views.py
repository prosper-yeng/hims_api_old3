# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    ProcedureChargeBySponsorSerializer,
    CombinedProcedureChargeBySponsorSerializer,
)
from .models import ProcedureChargeBySponsor


class ProcedureChargeBySponsorViewSet(viewsets.ModelViewSet):
    queryset = ProcedureChargeBySponsor.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProcedureChargeBySponsorSerializer


class CombinedProcedureChargeBySponsorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = ProcedureChargeBySponsor.objects.all()
        serialized = CombinedProcedureChargeBySponsorSerializer(query_data, many=True)
        return Response(serialized.data)
