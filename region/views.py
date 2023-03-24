from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegionSerializer, CombinedRegionNationSerializer
from .models import Region


class RegionViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CombinedRegionNationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = Region.objects.all()
        serialized = CombinedRegionNationSerializer(query_data, many=True)
        return Response(serialized.data)
