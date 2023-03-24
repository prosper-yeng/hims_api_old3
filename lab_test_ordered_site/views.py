# Create your views here.
from requests import Response
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import LabTestOrderedSiteSerializer, CombinedSerializer
from .models import LabTestOrderedSite


class LabTestOrderedSiteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestOrderedSite.objects.all()
    serializer_class = LabTestOrderedSiteSerializer


class CombinedLabTestOrderedSiteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = LabTestOrderedSite.objects.all()
        serialized = CombinedSerializer(query_data, many=True)
        return Response(serialized.data)
