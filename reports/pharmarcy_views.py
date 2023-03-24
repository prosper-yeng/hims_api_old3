from rest_framework import generics
from django.utils import timezone
# from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from prescription.models import Prescription
from prescription.serializers import CombinedDiagnosisPrescriptionSerializer

from warehouse_stock.models import WarehouseStock
from warehouse_stock.serializers import WarehouseStockDetailSerializer

timezone_now = timezone.now()

class PrescriptionReportViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CombinedDiagnosisPrescriptionSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = Prescription.objects.all()

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)
        product_name = request.query_params.get("product_name", None)
        user_id = request.query_params.get("user_id", None)
        product_category_name = request.query_params.get("product_category_name", None)
        product_category_id = request.query_params.get("product_category_id", None)
        
        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Query by Product Name
        if product_name is not None:
            queryset = queryset.filter(warehouse_product__name=product_name)

        # Query by Product Category Name
        if product_category_name is not None:
            queryset = queryset.filter(warehouse_product__product_type__product_category__name=product_category_name)

        # Query by Product Category Id
        if product_category_id is not None:
            queryset = queryset.filter(warehouse_product__product_type__product_category__id=product_category_id)

        # Query by User ID
        if user_id is not None:
            queryset = queryset.filter(
                consultation_diagnosis__vital_sign__attendance__patient__user__id=user_id
            )

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)

class StockViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WarehouseStockDetailSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = WarehouseStock.objects.filter(warehouse_product__product_type__product_category__name="Pharmacy")
       
        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)
        is_expired = request.query_params.get("is_expired", None)
        category_id = request.query_params.get("category_id", None)
        product_type_id = request.query_params.get("product_type_id", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on__date=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Query by Category Id 
        if category_id is not None:
            queryset = queryset.filter(warehouse_product__product_type__product_category__id=category_id)

        # Query by Product Type 
        if product_type_id is not None:
            queryset = queryset.filter(warehouse_product__product_type__id = product_type_id)

        # Query expired warehouse stock products
        if is_expired is not None and is_expired == True:
            queryset = queryset.filter(expiry_date__lte=timezone_now)

        # Query non-expired warehouse stock products
        if is_expired is not None and is_expired == False:
            queryset = queryset.filter(expiry_date__gt=timezone_now) 

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)
