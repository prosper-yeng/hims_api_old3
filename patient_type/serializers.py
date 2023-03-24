# Python/django imports
from rest_framework import serializers

from .models import PatientType


class PatientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientType
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
