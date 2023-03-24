from rest_framework import serializers

from .models import MedicationBillDetail


class MedicationBillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationBillDetail
        fields = [
            "id",
            "medication_bill",
            "unit_price",
            "quantity",
            "discount",
            "is_deleted",
            "created_by",
        ]
        read_only_fields = ("id",)
