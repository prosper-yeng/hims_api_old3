from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import PhysicalExamination
from .serializers import PhysicalExaminationSerializer


class PhysicalExaminationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PhysicalExamination.objects.all()
    serializer_class = PhysicalExaminationSerializer
