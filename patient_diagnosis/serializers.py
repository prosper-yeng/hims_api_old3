from rest_framework import serializers
from .models import PatientDiagnosis
from treatment_plan.serializers import TreatmentPlanDetailsSerializer
from diagnosis.serializers import DiagnosisDetailSerializer
from nurses_note.serializers import NursesNoteDetailsSerializer

class PatientDiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDiagnosis
        fields = "__all__"
        read_only_fields = ["id"]


class PatientDiagnosisDetailsSerializer(serializers.ModelSerializer):
    treatment_plan = TreatmentPlanDetailsSerializer()
    diagnosis = DiagnosisDetailSerializer()
    nurses_note = NursesNoteDetailsSerializer()

    class Meta:
        model = PatientDiagnosis
        fields = "__all__"
        read_only_fields = ["id"]
