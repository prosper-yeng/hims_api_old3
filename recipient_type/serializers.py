from rest_framework import serializers

from .models import RecipientType


class RecipientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipientType
        fields = ["id", "name", "status", "created_by"]
        read_only_fields = ("id",)
