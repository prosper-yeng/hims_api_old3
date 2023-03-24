# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PaymentSerializer, CombinedPaymentPatientUserSerializer
from .models import Payment


class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class CombinedPaymentPatientUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = Payment.objects.all()
        serialized = CombinedPaymentPatientUserSerializer(query_data, many=True)
        return Response(serialized.data)
