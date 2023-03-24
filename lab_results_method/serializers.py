from rest_framework import serializers

from .models import LabResultsMethod


class LabResultsMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabResultsMethod
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
