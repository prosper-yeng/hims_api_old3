from rest_framework import serializers, fields
import datetime

from .models import TransactionType


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ["id", "name", "created_by"]
