# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .serializers import OpdBillPatientSerializer
from .models import OpdBillPatient


class OpdBillPatientViewSet(viewsets.ModelViewSet):
    queryset = OpdBillPatient.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OpdBillPatientSerializer
