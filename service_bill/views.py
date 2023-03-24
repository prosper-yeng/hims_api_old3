# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import ServiceBillSerializer
from .models import ServiceBill


class ServiceBillViewSet(viewsets.ModelViewSet):
    queryset = ServiceBill.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceBillSerializer
