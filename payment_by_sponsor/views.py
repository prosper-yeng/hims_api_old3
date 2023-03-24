# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PaymentBySponsorSerializer, CombinedPaymentSponsorSerializer
from .models import PaymentBySponsor


class PaymentBySponsorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PaymentBySponsor.objects.all()
    serializer_class = PaymentBySponsorSerializer


class CombinedPaymentSponsorView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = PaymentBySponsor.objects.all()
        serialized = CombinedPaymentSponsorSerializer(query_data, many=True)
        return Response(serialized.data)
