# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderBatchSerializer
from .models import OrderBatch


class OrderBatchViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OrderBatch.objects.all()
    serializer_class = OrderBatchSerializer
