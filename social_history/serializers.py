from rest_framework import serializers

from person.serializers import PatientSerializer
from treatment_plan.serializers import TreatmentPlanSerializer
from .models import SocialHistory


class SocialHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialHistory
        fields = "__all__"
        read_only_fields = ["id"]


class CombinedUserPatientSocialHistorySerializer(serializers.ModelSerializer):
    patient = PatientSerializer(many=False)
    treatment_plan = TreatmentPlanSerializer ( many=False )

    class Meta:
        model = SocialHistory
        fields = "__all__"
