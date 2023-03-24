# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .serializers import WorkFlowSerializer
from .models import WorkFlow


class WorkFlowViewSet(viewsets.ModelViewSet):
    queryset = WorkFlow.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = WorkFlowSerializer


class WorkFlowAccessLevelViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]
    serializer_class = WorkFlowSerializer

    def get_queryset(self):
        service = self.request.query_params.get("service", None)
        if service:
            queryset_original = WorkFlow.objects.filter(service_id=service)
            queryset = queryset_original

            group = self.request.query_params.get("group", None)
            if group is not None:
                queryset = queryset.filter(group_id=group)

            if queryset:
                access_level = queryset.first().access_level + 1
                queryset = queryset_original.filter(
                    service=service, access_level=access_level
                )
            else:
                queryset = queryset_original.filter(service=service, access_level=1)

            return queryset
