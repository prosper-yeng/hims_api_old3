from rest_framework import serializers

from currency_type.serializers import CurrencyTypeSerializer
from daily_attendance.serializers import DailyAttendanceSerializer
from procedure.serializers import ProcedureSerializer
from procedure_charge.serializers import ProcedureChargeSerializer
from procedure_charge_by_sponsor.serializers import ProcedureChargeBySponsorSerializer
from service.serializers import ServiceSerializer
from .models import ProcedureChargeBySponsor, ProcedureSchedule


class ProcedureScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureSchedule
        fields = [
            "id",
            "procedure_charge_by_sponsor",
            "procedure_charge",
            "attendance",
            "schedule_date",
            "created_by",
            "is_deleted",
            "status",
        ]

        read_only_fields = ("id",)


class CombinedProcedureScheduleSerializer(serializers.ModelSerializer):
    attendance = DailyAttendanceSerializer(many=False)
    procedure_charge_by_sponsor = ProcedureChargeBySponsorSerializer(many=False)
    procedure_charge = ProcedureChargeSerializer(many=False)

    class Meta:
        model = ProcedureSchedule
        fields = "__all__"
