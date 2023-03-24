# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicationTypeSerializer
from .models import MedicationType


class MedicationTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MedicationType.objects.all()
    serializer_class = MedicationTypeSerializer
