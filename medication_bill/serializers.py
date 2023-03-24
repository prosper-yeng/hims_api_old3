from rest_framework import serializers

from .models import MedicationBill


class MedicationBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationBill
        fields = [
            "id",
            "product",
            #   'transaction',
            "prescription",
            "patient",
            "unit_price",
            "quantity",
            "bill_date",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)
