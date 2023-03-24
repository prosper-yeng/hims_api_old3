# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LabTestSiteSerializer, CombinedLabTestSiteSerializer
from .models import LabTestSite


class LabTestSiteViewSet ( viewsets.ModelViewSet ):
    permission_classes = [IsAuthenticated]
    queryset = LabTestSite.objects.all ()
    serializer_class = LabTestSiteSerializer


class CombinedLabTestSiteView ( APIView ):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = LabTestSite.objects.all ()
        serialized = CombinedLabTestSiteSerializer ( query_data, many=True )
        return Response ( serialized.data )
