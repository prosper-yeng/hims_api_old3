from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import RadiologyType
from .serializers import RadiologyTypeSerializer


class RadiologyTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RadiologyType.objects.all()
    serializer_class = RadiologyTypeSerializer
