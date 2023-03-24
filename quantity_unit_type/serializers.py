from rest_framework import serializers

from .models import QuantityUnitType


class QuantityUnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityUnitType
        fields = ["id", "name", "is_base_unit", "is_deleted", "status", "created_by"]

        read_only_fields = ("id",)
