# Python/django imports
from rest_framework import serializers

# Local app imports
from .models import IntraHospitalPatientTransfer


class IntraHospitalPatientTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntraHospitalPatientTransfer
        fields = "__all__"
        read_only_fields = ["id"]
