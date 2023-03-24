from rest_framework import serializers
from .models import InterHospitalPatientTransfer


class InterHospitalPatientTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterHospitalPatientTransfer
        fields = "__all__"
        read_only_fields = ["id"]
