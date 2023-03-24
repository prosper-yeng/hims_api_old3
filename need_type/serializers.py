from rest_framework import serializers
from .models import NeedType


class NeedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeedType
        fields = "__all__"
        read_only_fields = ["id"]
