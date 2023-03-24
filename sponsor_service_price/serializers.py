from rest_framework import serializers, fields
import datetime

from .models import SponsorServicePrice


class SponsorServicePriceSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source="service.name", required=False)

    class Meta:
        model = SponsorServicePrice
        fields = [
            "id",
            "sponsor",
            "service",
            "service_name",
            "amount_allowed",
            "percentage_allowed",
            "is_deleted",
            "created_by",
            "created_on",
            "is_deleted",
            "status",
        ]
