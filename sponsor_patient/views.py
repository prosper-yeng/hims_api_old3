from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import SponsorPatient
from .serializers import SponsorPatientSerializer


class SponsorPatientViewset(viewsets.ModelViewSet):
    queryset = SponsorPatient.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SponsorPatientSerializer
