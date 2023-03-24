# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import VitalSignSerializer, CombinedPatientVitalSignSerializer
from .models import VitalSign
from rest_framework.response import Response
from rest_framework.views import APIView


class VitalSignViewSet(viewsets.ModelViewSet):
    queryset = VitalSign.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = VitalSignSerializer


class VitalSignDetailViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]
    serializer_class = VitalSignSerializer

    def get_queryset(self):
        trans_id = self.request.query_params.get("trans_id", None)
        queryset = VitalSign.objects.filter(transaction_id=trans_id)

        return queryset


class CombinedPatientVitalSignView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = VitalSign.objects.all()
        serialized = CombinedPatientVitalSignSerializer(query_data, many=True)
        return Response(serialized.data)
