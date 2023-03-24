from rest_framework import serializers
from .models import RadiologyProcedure


class RadiologyProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyProcedure
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
