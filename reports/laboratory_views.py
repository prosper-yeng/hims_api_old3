from rest_framework import generics
from django.db.models import Sum
from django.db.models import Count
from django.shortcuts import get_object_or_404

# from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from lab_test_order_details.models import LabTestOrderDetails
from lab_test_order_details.serializers import CombinedConsultationLabTestSerializer

from lab_test_results.models import LabTestResults
from lab_test_results.serializers import CombinedLabTestOderResultsSerializer


from warehouse_stock.models import WarehouseStock
from warehouse_stock.serializers import WarehouseStockDetailSerializer

from warehouse_product.models import WarehouseProduct


class LabsPerformedReportViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CombinedConsultationLabTestSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = []
        for lab_test in  LabTestOrderDetails.objects.iterator(chunk_size=50):
            if LabTestResults.objects.filter(lab_test_order_details__id=lab_test.id).exists():
                queryset.append(lab_test)
       
        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)
        doctor_id = request.query_params.get("doctor_id", None)
        
        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on__date=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Query by single DATE
        if doctor_id is not None:
            queryset = queryset.filter(created_by__id=doctor_id)

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)



class LabResultsOfPatientReportViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CombinedLabTestOderResultsSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = LabTestResults.objects.all()
       
        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)
        first_name = request.query_params.get("first_name", None)
        last_name = request.query_params.get("last_name", None)
        phone = request.query_params.get("phone", None)
        dob = request.query_params.get("date_of_birth", None)
       

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on__date=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Query by FIRST_NAME
        if first_name is not None:
            queryset = queryset.filter(lab_test_order_details__consultation__vital_sign__attendance__patient__user__first_name=first_name)

        # Query by LAST_NAME
        if last_name is not None:
            queryset = queryset.filter(lab_test_order_details__consultation__vital_sign__attendance__patient__user__last_name=last_name)

        # Query by PHONE
        if phone is not None:
            queryset = queryset.filter(lab_test_order_details__consultation__vital_sign__attendance__patient__user__primary_phone=phone)

        # Query by DOB
        if dob:
            queryset = queryset.filter(lab_test_order_details__consultation__vital_sign__attendance__patient__user__date_of_birth=dob)

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)


class StockReorderLevelReportViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WarehouseStockDetailSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = WarehouseStock.objects.all()
        
        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)
        batch_no = request.query_params.get("batch_no", None)
        warehouse_product_name= request.query_params.get("warehouse_product_name", None)
        warehouse_product_id = request.query_params.get("warehouse_product_id", None)
        product_type_id = request.query_params.get("product_type_id", None)
        product_type_name = request.query_params.get("product_type_name", None)

        # Query by stock batch_no
        if batch_no is not None:
            queryset = queryset.filter(batch_no=batch_no)

        if warehouse_product_name is not None:
            queryset = queryset.filter(warehouse_product__name=warehouse_product_name)

        if warehouse_product_id is not None:
            queryset = queryset.filter(warehouse_product__id=warehouse_product_id)    

        if product_type_id is not None:
            queryset = queryset.filter(warehouse_product__product_type__id=warehouse_product_id)     

        if product_type_name is not None:
            queryset = queryset.filter(warehouse_product__product_type__name = warehouse_product_name)
        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on__date=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        # Extrat fields if warehouse_product params were specified
        if warehouse_product_id is not None or warehouse_product_name is not None:
            data["total_order_quantity"] = queryset.aggregate(Sum("ordered_quantity"))
            data["current_quantity"] = queryset.aggregate(Sum("quantity"))
        return Response(data)


class LabTestReportView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CombinedLabTestOderResultsSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = LabTestResults.objects.all()
       
        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)
        first_name = request.query_params.get("first_name", None)
        last_name = request.query_params.get("last_name", None)
        phone = request.query_params.get("phone", None)
        dob = request.query_params.get("date_of_birth", None)
        most_frequent = request.query_params.get("most_frequent", None)
        
        # Most frequent
        if most_frequent is not None and most_frequent == True:
            queryset = queryset.annotate(count=Count("lab_test_order_details__lab_test__id")).order_by("count")
            
        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on__date=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Query by FIRST_NAME
        if first_name is not None:
            queryset = queryset.filter(lab_test_order_details__consultation__vital_sign__attendance__patient__user__first_name=first_name)

        # Query by LAST_NAME
        if last_name is not None:
            queryset = queryset.filter(lab_test_order_details__consultation__vital_sign__attendance__patient__user__last_name=last_name)

        # Query by PHONE
        if phone is not None:
            queryset = queryset.filter(lab_test_order_details__consultation__vital_sign__attendance__patient__user__primary_phone=phone)

        # Query by DOB
        if dob:
            queryset = queryset.filter(lab_test_order_details__consultation__vital_sign__attendance__patient__user__date_of_birth__date=dob)

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        

        return Response(data)

