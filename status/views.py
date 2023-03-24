# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import StatusSerializer
from .models import Status
from rest_framework.permissions import IsAuthenticated


class StatusViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
