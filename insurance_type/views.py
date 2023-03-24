# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import InsuranceTypeSerializer
from .models import InsuranceType


class InsuranceTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = InsuranceType.objects.all()
    serializer_class = InsuranceTypeSerializer
