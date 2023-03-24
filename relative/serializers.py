from rest_framework import serializers

from person.serializers import PatientSerializer, UserSerializer
from .models import Relative


class RelativeSerializer(serializers.ModelSerializer):
    relative_type_name = serializers.CharField(
        source="relative_type.name", required=False
    )

    class Meta:
        model = Relative
        fields = [
            "id",
            "relative_person",
            "patient",
            "relative_type_name",
            "relative_type",
            "status",
        ]


class CombinedUserPatientRelativeSerializer(serializers.ModelSerializer):
    relative_person = UserSerializer(many=False)
    patient = PatientSerializer(many=False)

    class Meta:
        model = Relative
        fields = "__all__"
