from rest_framework import serializers, fields
from .models import TransactionLog


class TransactionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionLog
        fields = ["id", "transaction", "action", "access_level", "note", "created_by"]


# class SubmitReadySerializer (serializers.ModelSerializer):
#
#     submit_ready = serializers.BooleanField()
#
#     class Meta:
#         model = TransactionLog
#         fields = ['submit_ready',]
