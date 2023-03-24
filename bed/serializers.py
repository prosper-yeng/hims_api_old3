from rest_framework import serializers
from .models import Bed


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
