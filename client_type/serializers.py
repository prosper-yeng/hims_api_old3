from rest_framework import serializers

from .models import ClientType


class ClientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientType
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
