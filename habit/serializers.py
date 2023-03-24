from rest_framework import serializers

from person.serializers import PatientSerializer
from treatment_plan.serializers import TreatmentPlanSerializer
from .models import Habit


class HabitSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ["id"]


class CombinedUserPatientHabitSerializer ( serializers.ModelSerializer ):
    patient = PatientSerializer ( many=False )
    treatment_plan = TreatmentPlanSerializer ( many=False )

    class Meta:
        model = Habit
        fields = "__all__"
