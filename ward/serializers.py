from rest_framework import serializers
from .models import Ward


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
