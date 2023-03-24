from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import InterHospitalPatientTransfer
from .serializers import InterHospitalPatientTransferSerializer


class InterHospitalPatientTransferViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = InterHospitalPatientTransfer.objects.all()
    serializer_class = InterHospitalPatientTransferSerializer
