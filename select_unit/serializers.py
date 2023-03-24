from rest_framework import serializers, fields
import datetime

from .models import SelectUnit


class SelectUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectUnit
        fields = [
            "id",
            "sign",
            "unit",
            "percentage",
            "measurement_location",
            "rate",
            "is_default",
            "is_min_value",
            "is_max_value",
            "status",
            "created_by",
        ]

    def to_representation(self, instance):
        data = super(SelectUnitSerializer, self).to_representation(instance)
        data.created_on = serializers.CharField(source="created_on")
        return data
