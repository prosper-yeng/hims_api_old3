from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ObstetricHistory
from .serializers import ObstetricHistorySerializer, CombinedUserPatientbstetricHistorySerializer


class ObstetricHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ObstetricHistory.objects.all()
    serializer_class = ObstetricHistorySerializer


class CombinedUserPatientObstetricHistoryView ( APIView ):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = ObstetricHistory.objects.all ()
        serialized = CombinedUserPatientbstetricHistorySerializer ( query_data, many=True )
        return Response ( serialized.data )