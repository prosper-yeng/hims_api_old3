from rest_framework import serializers

from .models import LabPriority


class LabPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = LabPriority
        fields = ["id", "urgency", "fasting_status", "status"]
