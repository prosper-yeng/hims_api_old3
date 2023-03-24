from rest_framework import serializers

from .models import LabTestType


class LabTestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestType
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
