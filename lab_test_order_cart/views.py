# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import LabTestOrderCartSerializer
from .models import LabTestOrderCart


class LabTestOrderCartViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestOrderCart.objects.all()
    serializer_class = LabTestOrderCartSerializer
