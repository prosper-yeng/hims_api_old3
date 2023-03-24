from rest_framework import serializers
from .models import RadiologyType


class RadiologyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyType
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
