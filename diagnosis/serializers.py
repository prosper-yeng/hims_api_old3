from rest_framework import serializers

from .models import Diagnosis
from status.serializers import StatusSerializer
from person.serializers import UserSerializer


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = [
            "id",
            "name",
            "gdrg",
            "icd_code",
            "description",
            "status",
            "created_by",
        ]

        read_only_fields = ("id",)


class DiagnosisDetailSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    created_by = UserSerializer()

    class Meta:
        model = Diagnosis
        fields = [
            "id",
            "name",
            "gdrg",
            "icd_code",
            "description",
            "status",
            "created_by",
        ]

        read_only_fields = ("id",)
