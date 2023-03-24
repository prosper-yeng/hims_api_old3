from rest_framework import serializers

from person.serializers import PatientSerializer
from treatment_plan.serializers import TreatmentPlanSerializer
from .models import FamilyHistory


class FamilyHistorySerializer ( serializers.ModelSerializer ):
    class Meta:
        model = FamilyHistory
        fields = "__all__"
        read_only_fields = ["id"]


class CombinedUserPatientFamilyHistorySerializer ( serializers.ModelSerializer ):
    patient = PatientSerializer ( many=False )
    treatment_plan = TreatmentPlanSerializer ( many=False )

    class Meta:
        model = FamilyHistory
        fields = "__all__"
