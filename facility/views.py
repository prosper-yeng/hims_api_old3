from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Facility
from .serializers import FacilitySerializer, CombinedUserFacilityTownSerializer


class FacilityViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class CombinedFaciltyTownView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = Facility.objects.all()
        serialized = CombinedUserFacilityTownSerializer(query_data, many=True)
        from rest_framework.response import Response

        return Response(serialized.data)
