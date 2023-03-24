from rest_framework import serializers

from .models import MedicationOrder


class MedicationOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationOrder
        fields = [
            "id",
            "medication",
            "order_quantity",
            "order_quantity_unit",
            "selling_quantity",
            "selling_quantity_unit",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)
