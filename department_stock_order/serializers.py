from rest_framework import serializers

from .models import DepartmentStockOrder
from quantity_unit_type.serializers import QuantityUnitTypeSerializer
from order_batch.serializers import OrderBatchSerializer


class DepartmentStockOrderSerializer(serializers.ModelSerializer):
    warehouse_product_name = serializers.CharField(
        source="warehouse_product.name", required=False
    )
    department_name = serializers.CharField(source="department.name", required=False)

    # order_quantity_unit_type_name = serializers.CharField ( source='quantity_unit_type.name', required=False )
    # supplied_quantity_unit_type_name = serializers.CharField ( source='quantity_unit_type.name', required=False )
    # order_batch_name = serializers.CharField ( source='order_batch.name', required=False)
    class Meta:
        model = DepartmentStockOrder
        fields = [
            "id",
            "department",
            "department_name",
            "warehouse_product",
            "warehouse_product_name",
            "order_quantity_unit_type",
            "order_quantity",
            "order_batch",
            "is_deleted",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)


class CombinedSerializer(serializers.ModelSerializer):
    order_quantity_unit_type = QuantityUnitTypeSerializer(many=False)
    order_batch = OrderBatchSerializer(many=False)

    class Meta:
        model = DepartmentStockOrder
        fields = "__all__"
