from rest_framework import serializers

from .models import ClinicType


class ClinicTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicType
        fields = [
            "id",
            "name",
            "specialty_code",
            "specialty_description",
            "status",
            "created_by",
        ]

        read_only_fields = ("id",)
