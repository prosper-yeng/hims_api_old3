from rest_framework import serializers, fields
import datetime

from .models import ServiceType


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ["id", "name", "is_deleted", "status", "created_by"]

        read_only_fields = ("id",)
