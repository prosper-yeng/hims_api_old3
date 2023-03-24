from rest_framework import serializers
from .models import VitalSignsMonitoring


class VitalSignsMonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSignsMonitoring
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
