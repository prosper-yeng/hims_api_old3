# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import DiagnosisSerializer
from .models import Diagnosis


class DiagnosisViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
