from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Admission
from .serializers import *


class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    #permission_classes = [IsAuthenticated]
    action_serializers = {
        "retrieve": AdmissionDetailedSerializer,
        "list": AdmissionDetailedSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, "action_serializers"):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(AdmissionViewSet, self).get_serializer_class()


class AdmissionSearchView(generics.ListAPIView):
    queryset = Admission.objects.all()
    serializer_class = CombinedConsultationDiagnosisAdmissionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    
    filterset_fields = [
        "consultation_diagnosis__vital_sign__attendance__patient__user__first_name",
        "consultation_diagnosis__vital_sign__attendance__patient__user__last_name",
        "consultation_diagnosis__vital_sign__attendance__patient__user__date_of_birth",
        "consultation_diagnosis__vital_sign__attendance__patient__user__primary_phone",
        "consultation_diagnosis__vital_sign__attendance__patient__user__id",
        "consultation_diagnosis__vital_sign__attendance__patient__user__national_id",
    ]
