from rest_framework import serializers
from .models import NursesNote
from person.serializers import PatientSerializer


class NursesNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NursesNote
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]


class NursesNoteDetailsSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = NursesNote
        exclude = ["created_at", "updated_at"]
        read_only_fields = ["id"]
