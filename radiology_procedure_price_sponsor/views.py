from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import RadiologyProcedurePriceSponsor
from .serializers import RadiologyProcedurePriceSponsorSerializer


class RadiologyProcedurePriceSponsorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RadiologyProcedurePriceSponsor.objects.all()
    serializer_class = RadiologyProcedurePriceSponsorSerializer
