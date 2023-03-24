from rest_framework import serializers

from .models import LabTestBill


class LabTestBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestBill
        fields = [
            "id",
            #   'transaction',
            "lab_test",
            "patient",
            "unit_price",
            "quantity",
            "bill_date",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)
