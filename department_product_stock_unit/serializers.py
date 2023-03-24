from rest_framework import serializers

from .models import DepartmentProductStockUnit


class DepartmentProductStockUnitSerializer(serializers.ModelSerializer):
    department_stock_name = serializers.CharField(
        source="department_stock_order.name", required=False
    )
    quantity_unit_type_name = serializers.CharField(
        source="quantity_unit_type.name", required=False
    )

    class Meta:
        model = DepartmentProductStockUnit
        fields = [
            "id",
            "department_stock",
            "department_stock_name",
            "quantity_unit_type",
            "quantity_unit_type_name",
            "quantity",
            "status",
            "is_deleted",
            "created_by",
        ]
        read_only_fields = ("id",)
