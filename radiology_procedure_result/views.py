from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import RadiologyProcedureResult
from .serializers import RadiologyProcedureResultSerializer


class RadiologyProcedureResultViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RadiologyProcedureResult.objects.all()
    serializer_class = RadiologyProcedureResultSerializer
