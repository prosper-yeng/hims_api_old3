from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import PatientType
from .serializers import PatientTypeSerializer


class PatientTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PatientType.objects.all()
    serializer_class = PatientTypeSerializer
