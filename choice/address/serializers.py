from rest_framework import serializers, fields
import datetime

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "user",
            "address_type",
            "town",
            "street",
            "postcode",
            "house_number",
            "digital_address",
            "created_by",
            "status",
        ]
