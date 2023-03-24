# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicationUnitOfMeasurementSerializer
from .models import MedicationUnitOfMeasurement


class MedicationUnitOfMeasurementViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MedicationUnitOfMeasurement.objects.all()
    serializer_class = MedicationUnitOfMeasurementSerializer
