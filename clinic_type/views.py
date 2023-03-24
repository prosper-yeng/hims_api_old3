# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import ClinicTypeSerializer
from .models import ClinicType


class ClinicTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ClinicType.objects.all()
    serializer_class = ClinicTypeSerializer
