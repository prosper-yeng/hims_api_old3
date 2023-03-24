from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TownSerializer, CombinedTownDistrictSerializer
from .models import Town


class TownViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class CombinedTownDistrictView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = Town.objects.all()
        serialized = CombinedTownDistrictSerializer(query_data, many=True)
        return Response(serialized.data)
