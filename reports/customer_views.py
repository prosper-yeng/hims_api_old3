from rest_framework import generics

# from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from supplier.models import Supplier
from supplier.serializers import SupplierSerializer

from buyer.models import Buyer
from buyer.serializers import BuyerSerializer

from client.models import Client
from client.serializers import ClientSerializer


class SuppliersReportViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SupplierSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = Supplier.objects.all()

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)


class BuyersReportViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BuyerSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = Buyer.objects.all()

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)


class ClientReportViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer
    http_method_names = ["get"]

    def get(self, request):
        queryset = Client.objects.all()

        date = request.query_params.get("date", None)
        start_date = request.query_params.get("start_date", None)
        end_date = request.query_params.get("end_date", None)

        # Query by single DATE
        if date is not None:
            queryset = queryset.filter(created_on=date)

        # Query by DATE range
        if start_date is not None and end_date is not None:
            queryset = queryset.filter(created_on__range=(start_date, end_date))

        # Extra fields for returned set
        queryset = self.serializer_class(queryset, many=True).data
        data = {"count": len(queryset), "data": queryset}

        return Response(data)
