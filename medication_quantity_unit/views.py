# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicationQuantityUnitSerializer
from .models import MedicationQuantityUnit


class MedicationQuantityUnitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MedicationQuantityUnit.objects.all()
    serializer_class = MedicationQuantityUnitSerializer
