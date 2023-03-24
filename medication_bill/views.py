# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicationBillSerializer
from .models import MedicationBill


class MedicationBillViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MedicationBill.objects.all()
    serializer_class = MedicationBillSerializer
