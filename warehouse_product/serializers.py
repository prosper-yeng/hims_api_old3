from rest_framework import serializers

from product_category.serializers import ProductCategorySerializer
from product_type.serializers import ProductTypeSerializer
from unit_of_measurement.serializers import UnitOfMeasurementSerializer
from warehouse.serializers import WarehouseSerializer
from .models import WarehouseProduct


class WarehouseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseProduct
        fields = [
            "id",
            "warehouse",
            #'product_category',
            "product_type",
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


class CombinedWarehouseProductSerializer(serializers.ModelSerializer):
    unit_of_measurement = UnitOfMeasurementSerializer(many=False)
    warehouse = WarehouseSerializer(many=False)
    # product_category = ProductCategorySerializer ( many=False )
    product_type = ProductTypeSerializer(many=False)

    class Meta:
        model = WarehouseProduct
        fields = "__all__"
