# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import QuantityUnitTypeSerializer
from .models import QuantityUnitType


class MedicationTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = QuantityUnitType.objects.all()
    serializer_class = QuantityUnitTypeSerializer
