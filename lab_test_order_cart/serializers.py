from rest_framework import serializers

from sample_type.serializers import SampleTypeSerializer
from site_type.serializers import SiteTypeSerializer
from .models import LabTestOrderCart


class LabTestOrderCartSerializer(serializers.ModelSerializer):
    patient_first_name = serializers.CharField(
        source="patient.user.first_name", required=False
    )
    patient_last_name = serializers.CharField(
        source="patient.user.last_name", required=False
    )

    class Meta:
        model = LabTestOrderCart
        fields = [
            "id",
            "patient",
            "patient_first_name",
            "patient_last_name",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)
