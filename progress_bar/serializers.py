from rest_framework import serializers, permissions
from rest_framework.response import Response
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.views import APIView

from daily_attendance.models import DailyAttendanceModel
from progress_bar.models import ProgressBar


class ProgressBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressBar
        fields = [
            "id",
            "attendance",
            "vital_sign",
            "consultation",
            "diagnosis",
            "lab",
            "procedure",
            "prescription",
            "medication",
            "registration_fee",
            "consultation_fee",
            "procedure_fee",
            "lab_bill",
            "medication_bill",
            #'end_opd'
            "status",
            "created_by",
        ]
        validators = [
            UniqueTogetherValidator(
                queryset=ProgressBar.objects.all(),
                fields=["service", "attendance"],
                message="Every attendance has only one service",
            )
        ]

        read_only_fields = ("id",)


class CombinedAttendanceProgressView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        query_data = DailyAttendanceModel.objects.all()
        serialized = ProgressBarSerializer(query_data, many=True)
        return Response(serialized.data)
