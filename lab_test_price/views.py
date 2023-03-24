# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import LabTestPriceSerializer
from .models import LabTestPrice


class LabTestPriceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestPrice.objects.all()
    serializer_class = LabTestPriceSerializer
