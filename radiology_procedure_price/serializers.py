from rest_framework import serializers
from .models import RadiologyProcedurePrice


class RadiologyProcedurePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyProcedurePrice
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
