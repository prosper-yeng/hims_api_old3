from rest_framework import serializers

from .models import MedicationDosage


class MedicationDosageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationDosage
        fields = [
            "id",
            "medication_unit_of_measurement",
            "dosage_type",
            "recommended_dosage",
            "created_by",
        ]
        read_only_fields = ("id",)
