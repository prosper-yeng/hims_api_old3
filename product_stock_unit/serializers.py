from rest_framework import serializers

from .models import ProductStockUnit


class ProductStockUnitSerializer(serializers.ModelSerializer):
    warehouse_stock_name = serializers.CharField(
        source="warehouse_stock.name", required=False
    )
    quantity_unit_type_name = serializers.CharField(
        source="quantity_unit_type.name", required=False
    )

    class Meta:
        model = ProductStockUnit
        fields = [
            "id",
            "warehouse_stock",
            "warehouse_stock_name",
            "quantity_unit_type",
            "quantity_unit_type_name",
            "quantity",
            "status",
            "is_deleted",
            "created_by",
        ]
        read_only_fields = ("id",)
