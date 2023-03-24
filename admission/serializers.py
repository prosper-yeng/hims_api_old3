# Python/django imports
from rest_framework import serializers

from consultation_diagnosis.models import ConsultationDiagnosis
from consultation_diagnosis.serializers import CombinedConsultedDiagnosedPatientSerializer
from diagnosis.serializers import DiagnosisSerializer
from vital_sign.serializers import CombinedPatientVitalSignSerializer
from ward.serializers import WardSerializer
from .models import Admission


class AdmissionSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Admission
        fields = "__all__"
        read_only_fields = ["id"]



class AdmissionDetailedSerializer(serializers.ModelSerializer):
    consultation_diagnosis = CombinedConsultedDiagnosedPatientSerializer()
    ward = WardSerializer()

    class Meta:
        model = Admission
        fields = "__all__"




class ConsultationDiagnosisSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = ConsultationDiagnosis
        fields = (
            "id",
            "consultation",
            # 'patient',
            "vital_sign",
            "diagnosis",
            "note",
            "is_confirmed",
            "created_by",
            "created_on",
            "status",
        )
        read_only_fields = ("id",)


class CombinedConsultedDiagnosedPatientsSerializer ( serializers.ModelSerializer ):
    vital_sign = CombinedPatientVitalSignSerializer ( many=False )
    diagnosis = DiagnosisSerializer ( many=False )

    class Meta:
        model = ConsultationDiagnosis
        fields = "__all__"


class CombinedConsultationDiagnosisAdmissionSerializer ( serializers.ModelSerializer ):
   
    consultation_diagnosis = CombinedConsultedDiagnosedPatientsSerializer ( many=False )

    class Meta:
        model = Admission
        fields = "__all__" 
        
