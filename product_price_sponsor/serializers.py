from rest_framework import serializers

from .models import ProductPriceSponsor


class ProductPriceSponsorSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="warehouse_product.name", required=False
    )
    sponsor_name = serializers.CharField(source="sponsor.name", required=False)

    class Meta:
        model = ProductPriceSponsor
        fields = [
            "id",
            "product",
            "product_name",
            "sponsor",
            "sponsor_name",
            "profit_margin",
            "vat",
            "other_tax",
            "price",
            "cost_price",
            "discount",
            "is_deleted",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)
