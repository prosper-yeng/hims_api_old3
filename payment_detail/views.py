# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import PaymentDetailSerializer
from .models import PaymentDetail


class PaymentDetailViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PaymentDetail.objects.all()
    serializer_class = PaymentDetailSerializer
