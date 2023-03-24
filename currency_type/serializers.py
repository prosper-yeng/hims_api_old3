from rest_framework import serializers

from .models import CurrencyType


class CurrencyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyType
        fields = ["id", "name", "usd_rate", "created_by"]

        read_only_fields = ("id",)
