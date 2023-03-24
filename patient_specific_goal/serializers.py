from rest_framework import serializers
from .models import PatientSpecificGoal
from treatment_plan.serializers import TreatmentPlanDetailsSerializer
from nurses_note.serializers import NursesNoteDetailsSerializer

class PatientSpecificGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientSpecificGoal
        fields = "__all__"
        read_only_fields = ["id"]


class PatientSpecificGoalDetailsSerializer(serializers.ModelSerializer):
    treatment_plan = TreatmentPlanDetailsSerializer()
    nurses_note = NursesNoteDetailsSerializer()

    class Meta:
        model = PatientSpecificGoal
        fields = "__all__"
        read_only_fields = ["id"]
