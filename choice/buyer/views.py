# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import BuyerSerializer
from .models import Buyer


class BuyerViewSet(viewsets.ModelViewSet):
    permission = IsAuthenticated
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
