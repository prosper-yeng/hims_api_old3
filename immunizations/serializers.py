# Python/django imports
from rest_framework import serializers

# Local app imports
from person.serializers import PatientSerializer
from treatment_plan.serializers import TreatmentPlanSerializer
from .models import Immunizations


class ImmunizationsSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Immunizations
        fields = "__all__"
        read_only_fields = ["id"]


class CombinedUserPatientImmunizationsSerializer ( serializers.ModelSerializer ):
    patient = PatientSerializer ( many=False )
    treatment_plan = TreatmentPlanSerializer ( many=False )
    class Meta:
        model = Immunizations
        fields = "__all__"
