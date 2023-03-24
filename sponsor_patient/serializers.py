from rest_framework import serializers, fields
import datetime

from sponsor.serializers import SponsorSerializer
from person.serializers import PatientSerializer
from .models import SponsorPatient


class SponsorPatientSerializer(serializers.ModelSerializer):
    # >consulting_room_name = serializers.CharField ( source='consulting_room.name', required=False )
    class Meta:
        model = SponsorPatient
        fields = [
            "id",
            "patient",
            "sponsor",
            "memberId",
            "copay_percentage",
            "bill_limit",
            "valid_from",
            "valid_to",
            "created_by",
            "created_on",
            "is_deleted",
            "status",
        ]


class SponsorPatientDetailSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    sponsor = SponsorSerializer()

    class Meta:
        model = SponsorPatient
        fields = ["__all__"]
        read_only_fields = ["id"]
