from rest_framework import serializers

from .models import OpdBillType


class OpdBillTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpdBillType
        fields = [
            "id",
            "name",
            "adult_price",
            "child_price",
            "created_by",
            "adult_discount",
            "child_discount",
        ]

        read_only_fields = ("id",)
