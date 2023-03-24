# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import LabPrioritySerializer
from .models import LabPriority
from rest_framework.permissions import IsAuthenticated


class LabPriorityViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabPriority.objects.all()
    serializer_class = LabPrioritySerializer
