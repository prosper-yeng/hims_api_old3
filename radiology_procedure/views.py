from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import RadiologyProcedure
from .serializers import RadiologyProcedureSerializer


class RadiologyProcedureViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RadiologyProcedure.objects.all()
    serializer_class = RadiologyProcedureSerializer
