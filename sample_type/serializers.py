from rest_framework import serializers

from .models import SampleType


class SampleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleType
        fields = ["id", "name", "status"]
