from rest_framework import serializers

from .models import SponsorType


class SponsorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorType
        fields = ["id", "name", "status", "created_by"]
        read_only_fields = ("id",)
