from rest_framework import serializers

from daily_attendance.serializers import (
    DailyAttendanceSerializer,
    CombinedPatientAttendanceSerializer,
)
from person.serializers import (
    UserSerializer,
    PatientSerializer,
    CombinedPatientSerializer,
)

# from transaction.models import Transaction
# from transaction_log.models import TransactionLog
from .models import VitalSign


class VitalSignSerializer(serializers.ModelSerializer):
    # select_unit_name = serializers.CharField ( source='select_unit.name', required=False )

    class Meta:
        model = VitalSign
        fields = "__all__"
        read_only_fields = ("id",)


class CombinedPatientVitalSignSerializer(serializers.ModelSerializer):
    # patient = CombinedPatientSerializer ( many=False )
    # attendance = DailyAttendanceSerializer ( many=False )
    # created_by = UserSerializer ( many=False )
    attendance = CombinedPatientAttendanceSerializer(many=False)

    class Meta:
        model = VitalSign
        fields = "__all__"
