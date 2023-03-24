from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Address
from .serializers import AddressSerializer
from rest_framework.permissions import IsAuthenticated


class AddressViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
