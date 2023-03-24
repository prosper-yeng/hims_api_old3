from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import AdditionalData
from .serializers import AdditionalDataSerializer


class AdditionalDataViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AdditionalData.objects.all()
    serializer_class = AdditionalDataSerializer
