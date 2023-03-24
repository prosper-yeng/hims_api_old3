# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import RecommendedDosageSerializer
from .models import RecommendedDosage


class RecommendedDosageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RecommendedDosage.objects.all()
    serializer_class = RecommendedDosageSerializer
