from rest_framework import serializers, fields
import datetime

from .models import SelectItem


class SelectItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectItem
        fields = [
            "id",
            "type",
            "value",
            "text",
            "parent",
            "parent_name",
            "secured",
            "created_by",
        ]

    def to_representation(self, instance):
        data = super(SelectItemSerializer, self).to_representation(instance)
        data.created_on = serializers.CharField(source="created_on")
        return data
