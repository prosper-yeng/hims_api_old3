# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    DiagnosedProcedureSerializer,
    CombinedDiagnosisProcedureSerializer,
)
from .models import DiagnosedProcedure


class DiagnosedProcedureViewSet(viewsets.ModelViewSet):
    queryset = DiagnosedProcedure.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DiagnosedProcedureSerializer


class CombinedDiagnosedProcedureView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = DiagnosedProcedure.objects.all()
        serialized = CombinedDiagnosisProcedureSerializer(query_data, many=True)
        return Response(serialized.data)


"""
class DiagnosedProcedureDetailViewSet ( viewsets.ModelViewSet ):
    http_method_names = ['get']
    permission = [
        permissions.AllowAny
    ]
    serializer_class = DiagnosedProcedureSerializer

    def get_queryset(self):
        trans_id = self.request.query_params.get ( 'trans_id', None )
        queryset = DiagnosedProcedure.objects.filter ( transaction_id=trans_id )

        return queryset
"""
