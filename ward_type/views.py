from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import WardType
from .serializers import WardTypeSerializer


class WardTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = WardType.objects.all()
    serializer_class = WardTypeSerializer
