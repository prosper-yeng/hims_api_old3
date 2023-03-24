from rest_framework import serializers

from consultation_diagnosis.models import ConsultationDiagnosis
from daily_attendance.serializers import CombinedPatientAttendanceSerializer
from diagnosis.serializers import DiagnosisSerializer
from person.serializers import PatientSerializer
from vital_sign.serializers import CombinedPatientVitalSignSerializer


class ConsultationDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationDiagnosis
        fields = "__all__"
        read_only_fields = ("id",)


class CombinedConsultedDiagnosedPatientSerializer(serializers.ModelSerializer):
    # attendance = CombinedPatientAttendanceSerializer ( many=False )
    vital_sign = CombinedPatientVitalSignSerializer(many=False)
    diagnosis = DiagnosisSerializer(many=False)

    class Meta:
        model = ConsultationDiagnosis
        fields = "__all__"
