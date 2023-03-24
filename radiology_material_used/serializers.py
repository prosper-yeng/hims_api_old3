from rest_framework import serializers
from .models import RadiologyMaterialUsed


class RadiologyMaterialUsedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyMaterialUsed
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
