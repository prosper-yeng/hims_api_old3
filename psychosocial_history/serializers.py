from rest_framework import serializers

from person.serializers import PatientSerializer
from treatment_plan.serializers import TreatmentPlanSerializer
from .models import PsychosocialHistory


class PsychosocialHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychosocialHistory
        fields = "__all__"
        read_only_fields = ["id"]


class CombinedUserPatientPsychosocialHistorySerializer ( serializers.ModelSerializer ):
    patient = PatientSerializer ( many=False )
    treatment_plan = TreatmentPlanSerializer ( many=False )

    class Meta:
        model = PsychosocialHistory
        fields = "__all__"