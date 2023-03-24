from rest_framework import serializers, fields
import datetime

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
