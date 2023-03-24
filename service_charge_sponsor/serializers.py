from rest_framework import serializers

from currency_type.serializers import CurrencyTypeSerializer
from service.serializers import ServiceSerializer
from .models import ServiceChargeSponsor


class ServiceChargeSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceChargeSponsor
        fields = [
            "id",
            "service",
            "sponsor",
            "price",
            "currency_type",
            "percentage_allowed",
            "created_by",
            "is_deleted",
            "status",
        ]

        read_only_fields = ("id",)


class CombinedServiceChargeSponsorSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=False)
    currency_type = CurrencyTypeSerializer(many=False)

    class Meta:
        model = ServiceChargeSponsor
        fields = "__all__"
