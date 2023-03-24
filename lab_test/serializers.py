from rest_framework import serializers

from lab_test_type.serializers import LabTestTypeSerializer
from .models import LabTest


class LabTestSerializer(serializers.ModelSerializer):
    test_sites = serializers.CharField(source="lab_test.test_sites", required=False)

    class Meta:
        model = LabTest
        fields = [
            "id",
            "lab_test_type",
            "name",
            "test_sites",
            "description",
            "icd",
            "drg",
            "price",
            "created_by",
        ]
        read_only_fields = ("id",)


class CombinedLabTestTypeSerializer(serializers.ModelSerializer):
    lab_test_type=LabTestTypeSerializer(many=False)


    class Meta:
        model = LabTest
        fields = "__all__"