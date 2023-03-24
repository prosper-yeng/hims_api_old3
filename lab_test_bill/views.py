# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import LabTestBillSerializer
from .models import LabTestBill


class LabTestBillViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestBill.objects.all()
    serializer_class = LabTestBillSerializer
