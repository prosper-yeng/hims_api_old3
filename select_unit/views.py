# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import SelectUnitSerializer
from .models import SelectUnit


class SelectUnitViewset(viewsets.ModelViewSet):
    queryset = SelectUnit.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SelectUnitSerializer
