# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductStockUnitSerializer
from .models import ProductStockUnit


class ProductStockUnitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductStockUnit.objects.all()
    serializer_class = ProductStockUnitSerializer
