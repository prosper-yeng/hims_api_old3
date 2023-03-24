# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import AttendanceTypeSerializer
from .models import AttendanceType


class AttendanceTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AttendanceType.objects.all()
    serializer_class = AttendanceTypeSerializer
