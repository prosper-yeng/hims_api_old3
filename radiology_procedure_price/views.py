from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import RadiologyProcedurePrice
from .serializers import RadiologyProcedurePriceSerializer


class RadiologyProcedurePriceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RadiologyProcedurePrice.objects.all()
    serializer_class = RadiologyProcedurePriceSerializer
