from rest_framework import serializers, fields
import datetime

from .models import RelativeType


class RelativeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelativeType
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
