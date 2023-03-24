from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import PatientNeeds
from .serializers import PatientNeedsSerializer


class PatientNeedsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PatientNeeds.objects.all()
    serializer_class = PatientNeedsSerializer
