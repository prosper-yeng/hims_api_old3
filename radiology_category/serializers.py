from rest_framework import serializers
from .models import RadiologyCategory


class RadiologyCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RadiologyCategory
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
