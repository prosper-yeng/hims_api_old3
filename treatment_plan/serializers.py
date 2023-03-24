from rest_framework import serializers
from .models import TreatmentPlan
from person.serializers import PatientSerializer


class TreatmentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentPlan
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]


class TreatmentPlanDetailsSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = TreatmentPlan
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
