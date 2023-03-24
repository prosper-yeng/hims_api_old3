from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import WorkFlow


class WorkFlowSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source="service", required=False)
    group_name = serializers.CharField(source="group", required=False)

    class Meta:
        model = WorkFlow
        fields = [
            "id",
            "service",
            "group",
            "access_level",
            "created_by",
            "service_name",
            "group_name",
        ]
        validators = [
            UniqueTogetherValidator(
                queryset=WorkFlow.objects.all(),
                fields=["service", "group", "access_level"],
                message="Every service has only one access level per group",
            )
        ]

        read_only_fields = ("id",)
