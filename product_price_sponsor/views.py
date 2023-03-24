# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import ProductPriceSponsorSerializer
from .models import ProductPriceSponsor


class ProductPriceSponsorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductPriceSponsor.objects.all()
    serializer_class = ProductPriceSponsorSerializer
