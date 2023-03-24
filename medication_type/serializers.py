from rest_framework import serializers

from .models import MedicationType


class MedicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationType
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
