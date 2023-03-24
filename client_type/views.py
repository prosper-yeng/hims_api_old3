# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import ClientTypeSerializer
from .models import ClientType


class ClientTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer
