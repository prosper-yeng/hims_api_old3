from rest_framework import serializers

from product_category.serializers import ProductCategorySerializer
from .models import ProductType


class ProductTypeSerializer(serializers.ModelSerializer):
    product_category_name = serializers.CharField(
        source="product_category.name", required=False
    )

    class Meta:
        model = ProductType
        fields = [
            "id",
            "name",
            "description",
            "product_category_name",
            "product_category",
            "status",
            "is_deleted",
            "created_by",
        ]

        read_only_fields = ("id",)


class CombinedProductCategoryTypeSerializer(serializers.ModelSerializer):
    product_category = ProductCategorySerializer(many=False)

    class Meta:
        model = ProductType
        fields = "__all__"


class GroupProductCategoryTypeSerializer(serializers.ModelSerializer):
    # product_category = serializers.CharField ( source='product_category__name' )
    # count_category = serializers.IntegerField ()

    class Meta:
        model = ProductType
        fields = "__all__"
