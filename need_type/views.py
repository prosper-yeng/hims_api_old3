from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import NeedType
from .serializers import NeedTypeSerializer


class NeedTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = NeedType.objects.all()
    serializer_class = NeedTypeSerializer
