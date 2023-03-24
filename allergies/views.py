# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView

from person.models import Patient
from .serializers import AllergiesSerializer, CombinedUserPatientAllergiesSerializer
from .models import Allergies
from rest_framework.permissions import IsAuthenticated


class AllergiesViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Allergies.objects.all()
    serializer_class = AllergiesSerializer


class CombinedUserPatientAllergiesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = Allergies.objects.all()
        serialized = CombinedUserPatientAllergiesSerializer(query_data, many=True)
        return Response(serialized.data)
