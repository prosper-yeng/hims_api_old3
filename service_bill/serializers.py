from rest_framework import serializers

from .models import ServiceBill


class ServiceBillSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source="service", required=False)
    currency_type_name = serializers.CharField(source="currency_type", required=False)

    class Meta:
        model = ServiceBill
        fields = [
            "id",
            "service",
            #   'transaction',
            "amount",
            "currency_type",
            "created_by",
            "service_name",
            "currency_type_name",
        ]

        read_only_fields = ("id",)
