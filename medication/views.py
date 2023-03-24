# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicationSerializer
from .models import Medication


class MedicationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
