from rest_framework import serializers

from .models import SiteType


class SiteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteType
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
