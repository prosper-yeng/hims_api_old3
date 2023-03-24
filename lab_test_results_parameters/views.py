# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import LabTestResultsParametersSerializer
from .models import LabTestResultsParameters


class LabTestResultsParametersViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = LabTestResultsParameters.objects.all()
    serializer_class = LabTestResultsParametersSerializer
