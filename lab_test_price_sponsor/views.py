# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import LabTestPriceSponsorSerializer
from .models import LabTestPriceSponsor


class LabTestPriceSponsorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestPriceSponsor.objects.all()
    serializer_class = LabTestPriceSponsorSerializer
