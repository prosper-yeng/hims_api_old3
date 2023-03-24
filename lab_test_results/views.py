# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import LabTestResultsSerializer, CombinedLabTestOderResultsSerializer
from .models import LabTestResults


class LabTestResultsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestResults.objects.all()
    serializer_class = LabTestResultsSerializer


class CombinedLabTestOrderResultView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = LabTestResults.objects.all()
        serialized = CombinedLabTestOderResultsSerializer(query_data, many=True)
        return Response(serialized.data)
