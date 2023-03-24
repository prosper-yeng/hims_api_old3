from rest_framework import serializers, fields
import datetime

from groups.models import Group


class GroupPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
        read_only_fields = [
            "id",
        ]
