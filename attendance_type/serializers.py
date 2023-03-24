from rest_framework import serializers

from .models import AttendanceType


class AttendanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceType
        fields = ["id", "name", "status", "created_by"]

        read_only_fields = ("id",)
