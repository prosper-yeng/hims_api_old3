from rest_framework import serializers

from .models import MedicationQuantityUnit


class MedicationQuantityUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationQuantityUnit
        fields = ["id", "medication_quantity", "unit_type", "quantity", "created_by"]
        read_only_fields = ("id",)
