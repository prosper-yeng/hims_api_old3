# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicationDosageSerializer
from .models import MedicationDosage


class MedicationDosageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MedicationDosage.objects.all()
    serializer_class = MedicationDosageSerializer
