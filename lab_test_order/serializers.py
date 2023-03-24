from rest_framework import serializers

from .models import LabTestOrder


class LabTestOrderSerializer(serializers.ModelSerializer):
    sample_type_name = serializers.CharField(source="sample_type.name", required=False)
    site_type_name = serializers.CharField(source="site_type.name", required=False)
    lab_test_name = serializers.CharField(source="lab_test.name", required=False)

    class Meta:
        model = LabTestOrder
        fields = [
            "id",
            "lab_test_order_cart",
            "lab_test",
            "lab_test_name",
            "urgency",
            "fasting_status",
            "sample_types",
            "site_types",
            "price",
            "discount",
            "is_deleted",
            "created_by",
        ]
        read_only_fields = ("id",)
