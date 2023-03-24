# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WarehouseProductSerializer, CombinedWarehouseProductSerializer
from .models import WarehouseProduct


class WarehouseProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = WarehouseProduct.objects.all()
    serializer_class = WarehouseProductSerializer


class CombinedWarehouseProductView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = WarehouseProduct.objects.all()
        serialized = CombinedWarehouseProductSerializer(query_data, many=True)
        return Response(serialized.data)
