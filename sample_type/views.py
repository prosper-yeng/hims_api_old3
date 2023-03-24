# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import SampleTypeSerializer
from .models import SampleType
from rest_framework.permissions import IsAuthenticated


class SampleTypeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SampleType.objects.all()
    serializer_class = SampleTypeSerializer
