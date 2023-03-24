# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import ModeOfPaymentSerializer
from .models import ModeOfPayment


class ModeOfPaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ModeOfPayment.objects.all()
    serializer_class = ModeOfPaymentSerializer
