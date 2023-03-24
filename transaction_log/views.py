# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .serializers import TransactionLogSerializer
from .models import TransactionLog


class TransactionLogViewSet(viewsets.ModelViewSet):
    queryset = TransactionLog.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionLogSerializer


class SubmitReadyViewSet(viewsets.ModelViewSet):
    http_method_names = ["get"]

    permission_classes = [IsAuthenticated]
    serializer_class = TransactionLogSerializer

    def get_queryset(self):
        trans_id = self.request.query_params.get("trans_id", None)
        level = self.request.query_params.get("access_level", None)
        queryset = TransactionLog.objects.filter(
            transaction_id=trans_id, access_level=level
        )

        return queryset
