# Create your views here.
from requests import Response
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import LabTestOrderedSampleSerializer, CombinedSerializer
from .models import LabTestOrderedSample


class LabTestOrderedSampleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestOrderedSample.objects.all()
    serializer_class = LabTestOrderedSampleSerializer


class CombinedLabTestOrderedSampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = LabTestOrderedSample.objects.all()
        serialized = CombinedSerializer(query_data, many=True)
        return Response(serialized.data)
