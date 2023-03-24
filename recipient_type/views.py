# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import RecipientTypeSerializer
from .models import RecipientType


class RecipientTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RecipientType.objects.all()
    serializer_class = RecipientTypeSerializer
