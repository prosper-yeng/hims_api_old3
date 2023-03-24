from rest_framework import serializers

from .models import TestConsumable


class TestConsumableSerializer(serializers.ModelSerializer):
    # result_category_name = serializers.CharField ( source='lab_test_results_category.name', required=False )

    class Meta:
        model = TestConsumable
        fields = [
            "id",
            "lab_test_order_details",
            "department_stock",
            "quantity",
            "unit_type",
            "created_by",
        ]
        read_only_fields = ("id",)
