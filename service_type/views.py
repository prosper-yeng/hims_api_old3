# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import ServiceTypeSerializer
from .models import ServiceType


class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ServiceTypeSerializer
