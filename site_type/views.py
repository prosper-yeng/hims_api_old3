# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import SiteTypeSerializer
from .models import SiteType


class SiteTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = SiteType.objects.all()
    serializer_class = SiteTypeSerializer
