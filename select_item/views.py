# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import SelectItemSerializer
from .models import SelectItem


class SelectItemViewset(viewsets.ModelViewSet):
    queryset = SelectItem.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SelectItemSerializer
