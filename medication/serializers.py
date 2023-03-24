from rest_framework import serializers

from .models import Medication

from person.serializers import PatientSerializer
from daily_attendance.serializers import DailyAttendanceSerializer
from prescription.serializers import CombinedDiagnosisPrescriptionSerializer


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = [
            "id",
            "patient",
            "attendance",
            "sponsor",
            "prescription",
            "product",
            "remark",
            "created_on",
            "created_by",
        ]
        read_only_fields = ("id",)


class MedicationDetailSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    attendance = DailyAttendanceSerializer()
    prescription = CombinedDiagnosisPrescriptionSerializer()

    class Meta:
        model = Medication
        fields = "__all__"
        read_only_fields = ("id",)
