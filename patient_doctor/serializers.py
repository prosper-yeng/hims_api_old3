from rest_framework import serializers

from .models import PatientDoctor


class PatientDoctorSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source="patient", required=False)
    doctor_name = serializers.CharField(source="doctor", required=False)

    class Meta:
        model = PatientDoctor
        fields = (
            "id",
            "patient",
            "patient_name",
            "doctor",
            "doctor_name",
            "is_current",
            "created_by",
        )

        read_only_fields = ("id",)
