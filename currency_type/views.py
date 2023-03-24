# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import CurrencyTypeSerializer
from .models import CurrencyType


class CurrencyTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = CurrencyType.objects.all()
    serializer_class = CurrencyTypeSerializer
