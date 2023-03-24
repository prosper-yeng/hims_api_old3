from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import SponsorServicePrice
from .serializers import SponsorServicePriceSerializer


class SponsorServicePriceViewset(viewsets.ModelViewSet):
    queryset = SponsorServicePrice.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SponsorServicePriceSerializer
