# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import TransactionTypeSerializer
from .models import TransactionType


class TransactionTypeViewset(viewsets.ModelViewSet):
    queryset = TransactionType.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransactionTypeSerializer
