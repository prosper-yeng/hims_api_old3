# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import LabTestResultsUploadSerializer
from .models import LabTestResultsUpload


class LabTestResultsUploadViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestResultsUpload.objects.all()
    serializer_class = LabTestResultsUploadSerializer
