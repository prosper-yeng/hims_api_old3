from rest_framework import serializers
from .models import PhysicalExamination


class PhysicalExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalExamination
        fields = "__all__"
        read_only_fields = ["id"]
