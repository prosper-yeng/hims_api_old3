# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import SponsorTypeSerializer
from .models import SponsorType


class SponsorTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SponsorType.objects.all()
    serializer_class = SponsorTypeSerializer
