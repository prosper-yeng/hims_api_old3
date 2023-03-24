from rest_framework import serializers

from consultation_diagnosis.models import ConsultationDiagnosis
from daily_attendance.serializers import CombinedPatientAttendanceSerializer
from diagnosed_procedure.models import DiagnosedProcedure
from diagnosis.serializers import DiagnosisSerializer
from procedure.serializers import ProcedureSerializer
from vital_sign.serializers import CombinedPatientVitalSignSerializer


class DiagnosedProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosedProcedure
        fields = (
            "id",
            "consultation_diagnosis",
            "price",
            "sponsor",
            "procedure",
            "note",
            "created_by",
            "status",
        )

        read_only_fields = ("id",)


class ConsultationDiagnosisSerializer(serializers.ModelSerializer):
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


class CombinedConsultedDiagnosedPatientSerializer(serializers.ModelSerializer):
    vital_sign = CombinedPatientVitalSignSerializer(many=False)
    diagnosis = DiagnosisSerializer(many=False)

    class Meta:
        model = ConsultationDiagnosis
        fields = "__all__"


class CombinedDiagnosisProcedureSerializer(serializers.ModelSerializer):
    procedure = ProcedureSerializer(many=False)
    consultation_diagnosis = CombinedConsultedDiagnosedPatientSerializer(many=False)

    class Meta:
        model = DiagnosedProcedure
        fields = "__all__"
