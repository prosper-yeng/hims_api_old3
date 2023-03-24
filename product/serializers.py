from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    product_type_name = serializers.CharField(
        source="product_type.name", required=False
    )
    unit_of_measurement_name = serializers.CharField(
        source="unit_of_measurement.name", required=False
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "product_type_name",
            "product_type",
            "unit_of_measurement_name",
            "unit_of_measurement",
            "name",
            "bar_code",
            "description",
            "brand",
            "icd_code",
            "side_effect",
            "serial_number",
            "status",
            "is_deleted",
            "created_by",
        ]
        read_only_fields = ("id",)
