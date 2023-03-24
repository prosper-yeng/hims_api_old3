from rest_framework import serializers

from .models import PrescriptionDosage


class PrescriptionDosageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionDosage
        fields = ["id", "prescription", "quantity", "time", "status", "created_by"]
        read_only_fields = ("id",)
