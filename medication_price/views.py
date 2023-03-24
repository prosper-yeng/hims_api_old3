# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicationPriceSerializer
from .models import MedicationPrice


class MedicationPriceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MedicationPrice.objects.all()
    serializer_class = MedicationPriceSerializer
