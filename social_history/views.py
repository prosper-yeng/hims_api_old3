from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SocialHistory
from .serializers import SocialHistorySerializer, CombinedUserPatientSocialHistorySerializer


class SocialHistoryViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = SocialHistory.objects.all()
    serializer_class = SocialHistorySerializer

class CombinedUserPatientSocialHistoryView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = SocialHistory.objects.all()
        serialized = CombinedUserPatientSocialHistorySerializer(query_data, many=True)
        return Response(serialized.data)
