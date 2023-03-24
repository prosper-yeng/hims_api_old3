from rest_framework import serializers
from person.serializers import PatientSerializer
from .models import Allergies


class AllergiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergies
        fields = ["id", "patient", "nurses_note", "name", "description", "status"]


class CombinedUserPatientAllergiesSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(many=False)

    class Meta:
        model = Allergies
        fields = "__all__"
