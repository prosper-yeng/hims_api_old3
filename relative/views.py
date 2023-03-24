# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView

from person.models import Patient
from .serializers import RelativeSerializer, CombinedUserPatientRelativeSerializer
from .models import Relative
from rest_framework.permissions import IsAuthenticated


class RelativeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Relative.objects.all()
    serializer_class = RelativeSerializer


class CombinedUserPatientRelativeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = Relative.objects.all()
        serialized = CombinedUserPatientRelativeSerializer(query_data, many=True)
        return Response(serialized.data)
