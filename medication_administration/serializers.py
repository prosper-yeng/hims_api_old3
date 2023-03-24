from rest_framework import serializers
from .models import MedicationAdministration


class MedicationAdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationAdministration
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
