from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import RadiologyProcedureRequest
from .serializers import RadiologyProcedureRequestSerializer


class RadiologyProcedureRequestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RadiologyProcedureRequest.objects.all()
    serializer_class = RadiologyProcedureRequestSerializer
