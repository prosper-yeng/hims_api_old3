# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import DepartmentProductStockUnitSerializer
from .models import DepartmentProductStockUnit


class DepartmentProductStockUnitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DepartmentProductStockUnit.objects.all()
    serializer_class = DepartmentProductStockUnitSerializer
