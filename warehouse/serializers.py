from rest_framework import serializers

from .models import Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["id", "name", "description", "status", "is_default", "created_by"]

        read_only_fields = ("id",)
