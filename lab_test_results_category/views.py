# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import LabTestResultsCategorySerializer
from .models import LabTestResultsCategory


class LabTestResultsCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestResultsCategory.objects.all()
    serializer_class = LabTestResultsCategorySerializer
