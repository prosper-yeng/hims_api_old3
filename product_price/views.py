# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductPriceSerializer
from .models import ProductPrice


class ProductPriceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer
