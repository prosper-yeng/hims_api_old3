# Python/django imports
from rest_framework import serializers

# Local app imports
from .models import DoctorsNote
from person.serializers import PatientSerializer


class DoctorsNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorsNote
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]


class DoctorsNoteDetailsSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = DoctorsNote
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
