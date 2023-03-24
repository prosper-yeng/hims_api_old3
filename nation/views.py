# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import NationalSerializer
from .models import Nation
from rest_framework.permissions import IsAuthenticated


class NationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Nation.objects.all()
    serializer_class = NationalSerializer
