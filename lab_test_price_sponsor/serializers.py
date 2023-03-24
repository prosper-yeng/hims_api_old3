from rest_framework import serializers

from .models import LabTestPriceSponsor


class LabTestPriceSponsorSerializer(serializers.ModelSerializer):
    lab_test_name = serializers.CharField(source="lab_test.name", required=False)
    sponsor_name = serializers.CharField(source="sponsor.name", required=False)

    class Meta:
        model = LabTestPriceSponsor
        fields = [
            "id",
            "lab_test",
            "lab_test_name",
            "sponsor",
            "sponsor_name",
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
