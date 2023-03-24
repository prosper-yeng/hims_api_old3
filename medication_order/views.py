# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicationOrderSerializer
from .models import MedicationOrder


class MedicationOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MedicationOrder.objects.all()
    serializer_class = MedicationOrderSerializer
