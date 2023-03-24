from rest_framework import serializers, fields
import datetime

from permission.serializers import PermissionSerializer
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            "id",
            "is_admin",
            "is_editor",
            "is_viewer",
            "is_superuser",
            "name",
            "permissions",
            "status",
        ]
        read_only_fields = [
            "id",
        ]
        # extra_kwargs = {'id': {'read_only': True}}

    # def to_representation(self, instance):
    #     data = super(GroupSerializer, self).to_representation(instance)
    #     data.created_on = serializers.CharField(source='created_on')
    #     return data


class GroupUpdateStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["status"]  # '__all__'


class CombinedGroupPermissionSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = "__all__"
