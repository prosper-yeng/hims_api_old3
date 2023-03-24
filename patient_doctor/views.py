# Create your views here.
from rest_framework import viewsets, permissions

from .serializers import PatientDoctorSerializer
from .models import PatientDoctor


class PatientDoctorViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctor.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientDoctorSerializer
