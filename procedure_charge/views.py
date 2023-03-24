# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CombinedProcedureChargeSerializer, ProcedureChargeSerializer
from .models import ProcedureCharge


class ProcedureChargeViewSet(viewsets.ModelViewSet):
    queryset = ProcedureCharge.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProcedureChargeSerializer


class CombinedProcedureChargeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = ProcedureCharge.objects.all()
        serialized = CombinedProcedureChargeSerializer(query_data, many=True)
        return Response(serialized.data)
