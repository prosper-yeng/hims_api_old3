# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LabTestSerializer, CombinedLabTestTypeSerializer
from .models import LabTest


class LabTestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTest.objects.all()
    serializer_class = LabTestSerializer

class CombinedLabTestTypeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = LabTest.objects.all()
        serialized = CombinedLabTestTypeSerializer(query_data, many=True)
        return Response(serialized.data)
