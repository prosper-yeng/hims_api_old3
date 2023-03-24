from rest_framework import serializers

from .models import MedicationUnitOfMeasurement


class MedicationUnitOfMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationUnitOfMeasurement
        fields = [
            "id",
            #'medication',
            "unit_of_measurement",
            "selling_unit",
            "created_by",
        ]
        read_only_fields = ("id",)
