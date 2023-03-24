from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import PsychosocialHistory
from .serializers import PsychosocialHistorySerializer, CombinedUserPatientPsychosocialHistorySerializer


class PsychosocialHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PsychosocialHistory.objects.all()
    serializer_class = PsychosocialHistorySerializer


class CombinedUserPatientPsychosocialHistoryView ( APIView ):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = PsychosocialHistory.objects.all ()
        serialized = CombinedUserPatientPsychosocialHistorySerializer ( query_data, many=True )
        return Response ( serialized.data )