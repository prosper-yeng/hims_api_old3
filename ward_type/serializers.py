from rest_framework import serializers
from .models import WardType


class WardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardType
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
