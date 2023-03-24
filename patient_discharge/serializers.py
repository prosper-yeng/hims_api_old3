# Python/django imports
from rest_framework import serializers
from patient_discharge.models import PatientDischarge


class PatientDischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDischarge
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
