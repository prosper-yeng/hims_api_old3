from rest_framework import serializers

from currency_type.serializers import CurrencyTypeSerializer
from service.serializers import ServiceSerializer
from .models import ServiceCharge


class ServiceChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCharge
        fields = [
            "id",
            "service",
            "price",
            "currency_type",
            "created_by",
            "is_deleted",
            "status",
        ]

        read_only_fields = ("id",)


class CombinedServiceChargeSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=False)
    currency_type = CurrencyTypeSerializer(many=False)

    class Meta:
        model = ServiceCharge
        fields = "__all__"
