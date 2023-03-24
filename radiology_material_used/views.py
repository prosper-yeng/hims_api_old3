from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import RadiologyMaterialUsed
from .serializers import RadiologyMaterialUsedSerializer


class RadiologyMaterialUsedViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RadiologyMaterialUsed.objects.all()
    serializer_class = RadiologyMaterialUsedSerializer
