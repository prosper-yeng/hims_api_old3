# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicationBillDetailSerializer
from .models import MedicationBillDetail


class MedicationBillDetailViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MedicationBillDetail.objects.all()
    serializer_class = MedicationBillDetailSerializer
