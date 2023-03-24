# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import TestConsumableSerializer
from .models import TestConsumable


class TestConsumableViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TestConsumable.objects.all()
    serializer_class = TestConsumableSerializer
