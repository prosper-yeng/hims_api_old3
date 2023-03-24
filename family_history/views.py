from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FamilyHistory
from .serializers import FamilyHistorySerializer, CombinedUserPatientFamilyHistorySerializer


class FamilyHistoryViewSet ( viewsets.ModelViewSet ):
    permission_classes = [IsAuthenticated]
    queryset = FamilyHistory.objects.all ()
    serializer_class = FamilyHistorySerializer


class CombinedUserPatientFamilyHistoryView ( APIView ):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = FamilyHistory.objects.all ()
        serialized = CombinedUserPatientFamilyHistorySerializer ( query_data, many=True )
        return Response ( serialized.data )
