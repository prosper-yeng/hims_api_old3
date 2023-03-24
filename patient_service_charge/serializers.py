from rest_framework import serializers

from currency_type.serializers import CurrencyTypeSerializer
from daily_attendance.serializers import DailyAttendanceSerializer
from service.serializers import ServiceSerializer
from sponsor.serializers import SponsorSerializer
from .models import PatientServiceCharge


class PatientServiceChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientServiceCharge
        fields = [
            "id",
            "service",
            "attendance",
            "price_individual",
            "price_sponsor",
            "sponsor",
            "patient",
            #'lab_test',
            #'medication',
            "is_paid",
            "invoice_id",
            "created_by",
            "is_deleted",
            "status",
        ]

        read_only_fields = ("id",)


class CombinedPatientServiceChargeSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=False)
    attendance = DailyAttendanceSerializer(many=False)
    sponsor = SponsorSerializer(many=False)

    class Meta:
        model = PatientServiceCharge
        fields = "__all__"
