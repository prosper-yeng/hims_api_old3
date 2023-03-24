# Create your views here.
from rest_framework import viewsets

from .serializers import MaritalStatusSerializer
from .models import MaritalStatus
from rest_framework.permissions import IsAuthenticated


class MaritalStatusViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer
