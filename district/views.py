# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DistrictSerializer, CombinedDistrictRegionSerializer
from .models import District


class DistrictViewset(viewsets.ModelViewSet):
    queryset = District.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DistrictSerializer


class CombinedDistrictRegionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = District.objects.all()
        serialized = CombinedDistrictRegionSerializer(query_data, many=True)
        return Response(serialized.data)
