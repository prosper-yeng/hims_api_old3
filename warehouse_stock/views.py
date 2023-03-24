# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import WarehouseStockSerializer
from .models import WarehouseStock


class WarehouseStockViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = WarehouseStock.objects.all()
    serializer_class = WarehouseStockSerializer
