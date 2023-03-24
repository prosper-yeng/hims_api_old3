from rest_framework import serializers
from .models import RadiologyProcedureResult


class RadiologyProcedureResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyProcedureResult
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
