from rest_framework import serializers

from person.serializers import PatientSerializer
from treatment_plan.serializers import TreatmentPlanSerializer
from .models import ObstetricHistory


class ObstetricHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ObstetricHistory
        fields = "__all__"
        read_only_fields = ["id"]


class CombinedUserPatientbstetricHistorySerializer ( serializers.ModelSerializer ):
    patient = PatientSerializer ( many=False )
    treatment_plan = TreatmentPlanSerializer ( many=False )
    class Meta:
        model = ObstetricHistory
        fields = "__all__"