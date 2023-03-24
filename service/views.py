# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from service_charge.models import ServiceCharge

# from work_flow.models import WorkFlow
from .serializers import ServiceSerializer, CombinedServiceTypeServiceSerializer
from .models import Service


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer


class CombinedServiceTypeServiceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        query_data = Service.objects.all()
        serialized = CombinedServiceTypeServiceSerializer(query_data, many=True)
        return Response(serialized.data)

    """class WorkflowServiceViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Service.objects.filter(in_workflow=True)

    permission = [
        permissions.AllowAny
    ]
    serializer_class = ServiceSerializer


class RegistrationServiceViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Service.objects.filter(in_workflow=True)

    # have only services that are already in the workflow
    workflow_service = WorkFlow.objects.values_list('service_id')
    queryset = queryset.filter(id__in=workflow_service)

    # have only services that has charges defined
    service_charge = ServiceCharge.objects.values_list('service_id')
    queryset = queryset.filter(id__in=service_charge)

    permission = [
        permissions.AllowAny
    ]
    serializer_class = ServiceSerializer

"""
