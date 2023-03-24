from rest_framework import serializers

from .models import LabTestResultsType


class LabTestResultsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestResultsType
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
