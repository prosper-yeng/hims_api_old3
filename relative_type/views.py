# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import RelativeTypeSerializer
from .models import RelativeType


class RelativeTypeViewSet(viewsets.ModelViewSet):
    queryset = RelativeType.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RelativeTypeSerializer
