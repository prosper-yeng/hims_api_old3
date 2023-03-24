from rest_framework import serializers, fields
import datetime

from service_type.serializers import ServiceTypeSerializer
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    # service_type_name = serializers.CharField(source='service_type', required=False)

    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "description",
            #'in_workflow',
            "created_by",
            "service_type",
            "is_deleted",
            "status",
        ]

    read_only_fields = ("id",)


class CombinedServiceTypeServiceSerializer(serializers.ModelSerializer):
    service_type = ServiceTypeSerializer(many=False)

    class Meta:
        model = Service
        fields = "__all__"  # ['id', 'name', 'service_type_name', ]
