# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ServiceChargeSerializer, CombinedServiceChargeSerializer
from .models import ServiceCharge


class ServiceChargeViewSet(viewsets.ModelViewSet):
    queryset = ServiceCharge.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceChargeSerializer


class CombinedServiceChargeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = ServiceCharge.objects.all()
        serialized = CombinedServiceChargeSerializer(query_data, many=True)
        return Response(serialized.data)
