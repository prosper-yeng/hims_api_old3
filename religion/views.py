# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import ReligionSerializer
from .models import Religion
from rest_framework.permissions import IsAuthenticated


class ReligionViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer
