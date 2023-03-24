from rest_framework import serializers

from .models import LabTestResultsCategory


class LabTestResultsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestResultsCategory
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
