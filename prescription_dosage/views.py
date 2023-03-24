# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import PrescriptionDosageSerializer
from .models import PrescriptionDosage


class PrescriptionDosageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PrescriptionDosage.objects.all()
    serializer_class = PrescriptionDosageSerializer
