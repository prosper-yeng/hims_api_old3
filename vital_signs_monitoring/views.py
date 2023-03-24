from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import VitalSignsMonitoring
from .serializers import VitalSignsMonitoringSerializer


class VitalSignsMonitoringViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = VitalSignsMonitoring.objects.all()
    serializer_class = VitalSignsMonitoringSerializer
