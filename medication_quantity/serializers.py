from rest_framework import serializers

from .models import MedicationQuantity


class MedicationQuantitySerializer(serializers.ModelSerializer):
    unit_type_name = serializers.CharField(
        source="quantity_unit_type.name", required=False
    )

    class Meta:
        model = MedicationQuantity
        fields = [
            "id",
            "medication",
            "unit_type",
            "unit_type_name",
            "supplier",
            "note",
            "quantity",
            "batch_no",
            "expiry_date",
            "created_by",
        ]
        read_only_fields = ("id",)
