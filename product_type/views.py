# Create your views here.
from django.db.models import Count
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product_category.models import ProductCategory
from product_category.serializers import ProductCategorySerializer
from .serializers import (
    ProductTypeSerializer,
    CombinedProductCategoryTypeSerializer,
    GroupProductCategoryTypeSerializer,
)
from .models import ProductType


class ProductTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class CombinedProductCategoryTypeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = ProductType.objects.all()
        serialized = CombinedProductCategoryTypeSerializer(query_data, many=True)
        return Response(serialized.data)


class GetProductCategoryByCategoryTypeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = ProductType.objects.values("product_category").annotate(
            total=Count("name")
        )  # .values('product_category__name','count_category')

        serialized = GroupProductCategoryTypeSerializer(query_data, many=True)
        return Response(serialized.data)
