# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import DosageTypeSerializer
from .models import DosageType


class DosageTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = DosageType.objects.all()
    serializer_class = DosageTypeSerializer
