from rest_framework import serializers

from .models import InsuranceType


class InsuranceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceType
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
