# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import SponsorSerializer
from .models import Sponsor


class SponsorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
