from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .serializers import PatientDischargeSerializer
from .models import PatientDischarge


class PatientDischargeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PatientDischarge.objects.all()
    serializer_class = PatientDischargeSerializer
