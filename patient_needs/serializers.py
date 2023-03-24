from rest_framework import serializers
from .models import PatientNeeds


class PatientNeedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientNeeds
        fields = "__all__"
        read_only_fields = ["id"]
