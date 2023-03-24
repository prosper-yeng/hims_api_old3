from rest_framework import serializers
from .models import RadiologyProcedureRequest


class RadiologyProcedureRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyProcedureRequest
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
