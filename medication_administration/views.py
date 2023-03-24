from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import MedicationAdministration
from .serializers import MedicationAdministrationSerializer


class MedicationAdministrationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MedicationAdministration.objects.all()
    serializer_class = MedicationAdministrationSerializer
