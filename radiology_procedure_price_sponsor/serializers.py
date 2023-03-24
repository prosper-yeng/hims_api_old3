from rest_framework import serializers
from .models import RadiologyProcedurePriceSponsor


class RadiologyProcedurePriceSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyProcedurePriceSponsor
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
