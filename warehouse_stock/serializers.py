from rest_framework import serializers

from .models import WarehouseStock
from warehouse_product.serializers import CombinedWarehouseProductSerializer
from supplier.serializers import SupplierSerializer
from quantity_unit_type.serializers import QuantityUnitTypeSerializer
from status.serializers import StatusSerializer

class WarehouseStockSerializer(serializers.ModelSerializer):
    warehouse_product_name = serializers.CharField(
        source="warehouse_product.name", required=False
    )
    supplier_name = serializers.CharField(source="supplier.name", required=False)
    quantity_unit_type_name = serializers.CharField(
        source="quantity_unit_type.name", required=False
    )

    class Meta:
        model = WarehouseStock
        fields = "__all__"
        read_only_fields = ("id", "ordered_quantity",)

class WarehouseStockDetailSerializer(serializers.ModelSerializer):
    warehouse_product = CombinedWarehouseProductSerializer()
    supplier = SupplierSerializer()
    quantity_unit_type = QuantityUnitTypeSerializer()
    status = StatusSerializer()
    class Meta:
        model = WarehouseStock
        fields = "__all__"
        read_only_fields = ["id", "ordered_quantity"]