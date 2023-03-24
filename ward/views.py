from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import Ward
from .serializers import WardSerializer


class WardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
