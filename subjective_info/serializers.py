from rest_framework import serializers
from .models import SubjectiveInfo


class SubjectiveInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectiveInfo
        fields = "__all__"
        read_only_fields = ["id"]
