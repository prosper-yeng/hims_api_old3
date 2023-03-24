# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import OccupationSerializer
from .models import Occupation
from rest_framework.permissions import IsAuthenticated


class OccupationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
