# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    PaymentDetailIndividualSerializer,
    CombinedPaymentDetailSerializer,
)
from .models import PaymentDetailIndividual


class PaymentDetailIndividualViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PaymentDetailIndividual.objects.all()
    serializer_class = PaymentDetailIndividualSerializer


class CombinedPaymentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = PaymentDetailIndividual.objects.all()
        serialized = CombinedPaymentDetailSerializer(query_data, many=True)
        return Response(serialized.data)
