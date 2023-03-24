from rest_framework import serializers

from .models import LabTestResultsParameters


class LabTestResultsParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestResultsParameters
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
