# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated


# from work_flow.models import WorkFlow
from .serializers import (
    TransactionSerializer,
    TransactionSubmitSerializer,
    MyTasksSerializer,
)
from .models import Transaction


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer


class TransactionSubmitViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSubmitSerializer


class MyTasksViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]
    serializer_class = MyTasksSerializer

    def get_queryset(self):
        queryset = Transaction.objects.filter(status="active")
        group = self.request.query_params.get("group", None)
        # access_level = WorkFlow.objects.filter(group=group).values_list('access_level')
        queryset = queryset.filter(assigned_group=group)

        return queryset
