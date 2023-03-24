# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .serializers import ProgressBarSerializer
from .models import ProgressBar


class ProgressBarViewSet(viewsets.ModelViewSet):
    queryset = ProgressBar.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProgressBarSerializer
