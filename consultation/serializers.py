from rest_framework import serializers
from consultation_diagnosis.models import ConsultationDiagnosis
from daily_attendance.models import DailyAttendanceModel
from daily_attendance.serializers import DailyAttendanceSerializer
from person.serializers import (
    CombinedPatientSerializer,
    UserSerializer,
    PatientSerializer,
)

# from transaction.models import Transaction
# from transaction_log.models import TransactionLog
from vital_sign.serializers import (
    VitalSignSerializer,
    CombinedPatientVitalSignSerializer,
)
from .models import VitalSign, Consultation


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = (
            "id",
            #'patient',
            "vital_sign",
            # 'attendance',
            "chief_complain",
            "objective",
            "note",
            "created_by",
            "created_on",
            "status",
        )

        read_only_fields = ("id",)


class CombinedConsultationVitalSignSerializer(serializers.ModelSerializer):
    vital_sign = CombinedPatientVitalSignSerializer(many=False)
    # vital_sign= VitalSignSerializer ( many=False )
    # patient = PatientSerializer ( many=False )
    # attendance = DailyAttendanceSerializer ( many=False )
    # created_by = UserSerializer ( many=False )

    class Meta:
        model = Consultation
        # depth=1
        fields = "__all__"
