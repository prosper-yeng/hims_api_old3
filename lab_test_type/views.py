# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import LabTestTypeSerializer
from .models import LabTestType


class LabTestTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestType.objects.all()
    serializer_class = LabTestTypeSerializer
