from rest_framework import serializers

from .models import LabTestPrice


class LabTestPriceSerializer(serializers.ModelSerializer):
    lab_test_name = serializers.CharField(source="lab_test.name", required=False)

    class Meta:
        model = LabTestPrice
        fields = [
            "id",
            "lab_test",
            "lab_test_name",
            "profit_margin",
            "vat",
            "other_tax",
            "cost_price",
            "price",
            "discount",
            "is_deleted",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)
