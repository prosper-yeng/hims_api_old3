# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import LabResultsMethodSerializer
from .models import LabResultsMethod


class LabResultsMethodViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabResultsMethod.objects.all()
    serializer_class = LabResultsMethodSerializer
