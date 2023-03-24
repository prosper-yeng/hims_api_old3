from rest_framework import serializers
from .models import AdditionalData


class AdditionalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalData
        fields = "__all__"
        read_only_fields = ["id"]
