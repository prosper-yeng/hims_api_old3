from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated

from .models import PatientReview
from .serializers import PatientReviewSerializer


class PatientReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PatientReview.objects.all()
    serializer_class = PatientReviewSerializer
