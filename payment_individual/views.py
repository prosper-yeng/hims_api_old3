# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PaymentIndividualSerializer, CombinedPaymentPatientSerializer
from .models import PaymentIndividual


class PaymentIndividualViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PaymentIndividual.objects.all()
    serializer_class = PaymentIndividualSerializer


class CombinedPaymentIndividualPatientView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = PaymentIndividual.objects.all()
        serialized = CombinedPaymentPatientSerializer(query_data, many=True)
        return Response(serialized.data)
