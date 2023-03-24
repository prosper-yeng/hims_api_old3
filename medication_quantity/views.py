# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicationQuantitySerializer
from .models import MedicationQuantity


class MedicationQuantityViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MedicationQuantity.objects.all()
    serializer_class = MedicationQuantitySerializer
