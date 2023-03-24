from rest_framework import serializers

from consultation.models import Consultation

from daily_attendance.serializers import (
    DailyAttendanceSerializer,
    CombinedPatientAttendanceSerializer,
)
from lab_test.serializers import LabTestSerializer
from lab_test_order_details.models import LabTestOrderDetails
from person.serializers import UserSerializer
from person.serializers import PatientSerializer
from site_type.serializers import SiteTypeSerializer

# from transaction.serializers import TransactionSerializer
from vital_sign.serializers import CombinedPatientVitalSignSerializer


class LabTestOrderDetailsSerializer(serializers.ModelSerializer):
    # patient_first_name = serializers.CharField ( source='patient.user.first_name', required=False )
    # patient_last_name = serializers.CharField ( source='patient.user.last_name', required=False )
    # lab_test_name = serializers.CharField ( source='lab_test.name', required=False )

    class Meta:
        model = LabTestOrderDetails
        fields = [
            "id",
            "consultation",
            # 'attendance',
            # 'patient',
            # 'patient_first_name',
            # 'patient_last_name',
            "lab_test",
            #'lab_test_name',
            "urgency",
            "fasting_status",
            "price",
            "discount",
            "is_lab_result_taken",
            "is_deleted",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)


class ConsultationSerializer(serializers.ModelSerializer):
    vital_sign = CombinedPatientVitalSignSerializer(many=False)

    class Meta:
        model = Consultation
        fields = (
            "id",
            # 'patient',
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


"""
class CombinedConsultationAttendanceSerializer ( serializers.ModelSerializer ):
    attendance = CombinedPatientAttendanceSerializer ( many=False )
    class Meta:
        model = Consultation
        fields = '__all__'
"""


class CombinedConsultationLabTestSerializer(serializers.ModelSerializer):
    # created_by = UserSerializer ( many=False )
    consultation = ConsultationSerializer(many=False)
    # patient = PatientSerializer ( many=False )
    # consultation = ConsultationSerializer ( many=False )
    lab_test = LabTestSerializer(many=False)

    class Meta:
        model = LabTestOrderDetails
        fields = "__all__"
