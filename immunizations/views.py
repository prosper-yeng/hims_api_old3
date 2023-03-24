# Python/Django imports
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

# Local app imports
from rest_framework.response import Response
from rest_framework.views import APIView

from psychosocial_history.models import PsychosocialHistory
from .models import Immunizations
from .serializers import ImmunizationsSerializer, CombinedUserPatientImmunizationsSerializer


class ImmunizationsViewSet(viewsets.ModelViewSet):
    queryset = Immunizations.objects.all()
    serializer_class = ImmunizationsSerializer
    permission_classes = [IsAuthenticated]


class CombinedUserPatientImmunizationsView ( APIView ):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = Immunizations.objects.all ()
        serialized = CombinedUserPatientImmunizationsSerializer ( query_data, many=True )
        return Response ( serialized.data )