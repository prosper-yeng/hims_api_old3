from rest_framework import serializers

from .models import ModeOfPayment


class ModeOfPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeOfPayment
        fields = ["id", "name", "created_by"]

        read_only_fields = ("id",)
