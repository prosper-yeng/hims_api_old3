from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import ProcedureCare
from .serializers import ProcedureCareSerializer


class ProcedureCareViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProcedureCare.objects.all()
    serializer_class = ProcedureCareSerializer
