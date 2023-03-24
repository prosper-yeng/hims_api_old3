# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .serializers import OpdBillTypeSerializer
from .models import OpdBillType


class OpdBillTypeViewSet(viewsets.ModelViewSet):
    queryset = OpdBillType.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OpdBillTypeSerializer
