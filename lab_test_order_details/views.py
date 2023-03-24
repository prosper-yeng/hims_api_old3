# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (
    LabTestOrderDetailsSerializer,
    CombinedConsultationLabTestSerializer,
)
from .models import LabTestOrderDetails


class LabTestOrderDetailsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestOrderDetails.objects.all()
    serializer_class = LabTestOrderDetailsSerializer


class CombinedLabTestOrderDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = LabTestOrderDetails.objects.all()
        serialized = CombinedConsultationLabTestSerializer(query_data, many=True)
        return Response(serialized.data)


class LabTestOrderDetailsSearchView(generics.ListAPIView):
    queryset = LabTestOrderDetails.objects.all()
    serializer_class = CombinedConsultationLabTestSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

    filterset_fields = [
        "consultation__vital_sign__attendance__patient__user__first_name",
        "consultation__vital_sign__attendance__patient__user__last_name",
        "consultation__vital_sign__attendance__patient__user__date_of_birth",
        "consultation__vital_sign__attendance__patient__user__primary_phone",
        "consultation__vital_sign__attendance__patient__user__id",
        "consultation__vital_sign__attendance__patient__user__national_id",
    ]
