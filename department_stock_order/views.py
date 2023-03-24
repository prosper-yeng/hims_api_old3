# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import DepartmentStockOrderSerializer, CombinedSerializer
from .models import DepartmentStockOrder


class DepartmentStockOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DepartmentStockOrder.objects.all()
    serializer_class = DepartmentStockOrderSerializer


class CombinedLDepartmentStockView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = DepartmentStockOrder.objects.all()
        serialized = CombinedSerializer(query_data, many=True)
        return Response(serialized.data)
