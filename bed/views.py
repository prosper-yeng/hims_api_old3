from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import Bed
from .serializers import BedSerializer


class BedViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
