# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    ServiceChargeSponsorSerializer,
    CombinedServiceChargeSponsorSerializer,
)
from .models import ServiceChargeSponsor


class ServiceChargeSponsorViewSet(viewsets.ModelViewSet):
    queryset = ServiceChargeSponsor.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceChargeSponsorSerializer


class CombinedServiceChargeSponsorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = ServiceChargeSponsor.objects.all()
        serialized = CombinedServiceChargeSponsorSerializer(query_data, many=True)
        return Response(serialized.data)
