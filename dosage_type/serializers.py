from rest_framework import serializers

from .models import DosageType


class DosageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosageType
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
