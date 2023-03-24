from rest_framework import serializers
from .models import InterventionImplementation
from nurses_note.serializers import NursesNoteDetailsSerializer
from intervention_type.serializers import InterventionTypeSerializer
from patient_specific_goal.serializers import PatientSpecificGoalDetailsSerializer


class InterventionImplementationSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = InterventionImplementation
        fields = "__all__"
        read_only_fields = ["id"]


class InterventionImplementationDetailsSerializer ( serializers.ModelSerializer ):
    nurses_note = NursesNoteDetailsSerializer ()
    intervention_type = InterventionTypeSerializer ()
    patient_specific_goal = PatientSpecificGoalDetailsSerializer ()

    class Meta:
        model = InterventionImplementation
        fields = "__all__"
        read_only_fields = ["id"]
