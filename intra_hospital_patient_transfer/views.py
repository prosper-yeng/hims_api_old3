# Python/Django imports
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

# Local app imports
from .models import IntraHospitalPatientTransfer
from .serializers import IntraHospitalPatientTransferSerializer


class IntraHospitalPatientTransferViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = IntraHospitalPatientTransfer.objects.all()
    serializer_class = IntraHospitalPatientTransferSerializer
