from rest_framework import serializers

from .models import UnitOfMeasurement


class UnitOfMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasurement
        fields = ["id", "name", "description", "status", "is_deleted", "created_by"]

        read_only_fields = ("id",)
