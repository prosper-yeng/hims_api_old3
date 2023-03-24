from rest_framework import serializers, fields

from person.serializers import PatientSerializer
from .models import DailyAttendanceModel


class DailyAttendanceSerializer(serializers.ModelSerializer):
    consulting_room_name = serializers.CharField(
        source="consulting_room.name", required=False
    )
    clinic_type_name = serializers.CharField(source="clinic_type.name", required=False)
    attendance_type_name = serializers.CharField(
        source="attendance_type.name", required=False
    )

    class Meta:
        model = DailyAttendanceModel
        fields = [
            "id",
            "patient",
            "date_of_visit",
            "attendance_type_name",
            "clinic_type_name",
            "OpdNo",
            "relative",
            "sponsor",
            "clinic",
            "attendance_type",
            "copay",
            "created_by",
            "vital_sign_taken",
            "ccc",
            "consulting_room_name",
            "status",
        ]


class CombinedPatientAttendanceSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(many=False)
    # marital_status = MaritalStatusSerializer ( many=False )
    # title = PersonTitleSerializer ( many=False )
    # occupation = OccupationSerializer ( many=False )
    # religion = ReligionSerializer ( many=False )

    class Meta:
        model = DailyAttendanceModel
        fields = "__all__"
