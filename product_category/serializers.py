from rest_framework import serializers

from .models import ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ["id", "name", "description", "status", "is_deleted", "created_by"]

        read_only_fields = ("id",)
