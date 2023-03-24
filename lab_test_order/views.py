# Django/DRF imports
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Local app imports
from .serializers import LabTestOrderSerializer
from .models import LabTestOrder


class LabTestOrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestOrder.objects.all()
    serializer_class = LabTestOrderSerializer


class LabTestOrderSearchView(generics.ListAPIView):
    queryset = LabTestOrder.objects.all()
    serializer_class = LabTestOrderSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "labtestorder__lab_test_order_cart",
        "labtestorder__urgency",
        "labtestorder__fasting_status",
        "labtestorder__status",
    ]
