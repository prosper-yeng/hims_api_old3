from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import RadiologyCategory
from .serializers import RadiologyCategorySerializer


class RadiologyCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RadiologyCategory.objects.all()
    serializer_class = RadiologyCategorySerializer
