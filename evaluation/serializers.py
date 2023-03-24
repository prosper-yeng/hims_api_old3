from rest_framework import serializers
from .models import Evaluation
from nurses_note.serializers import NursesNoteDetailsSerializer
from intervention_implementation.serializers import InterventionImplementationDetailsSerializer
from patient_specific_goal.serializers import PatientSpecificGoalDetailsSerializer
from treatment_plan.serializers import TreatmentPlanDetailsSerializer


class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = "__all__"
        read_only_fields = ["id"]


class EvaluationDetailsSerializer(serializers.ModelSerializer):
    nurses_note = NursesNoteDetailsSerializer()
    intervention_implementation = InterventionImplementationDetailsSerializer()
    patient_specific_goal = PatientSpecificGoalDetailsSerializer()
    treatment_plan = TreatmentPlanDetailsSerializer()

    class Meta:
        model = Evaluation
        fields = "__all__"
        read_only_fields = ["id"]
