from rest_framework import serializers

from .models import RecommendedDosage


class RecommendedDosageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedDosage
        fields = [
            "id",
            "medication",
            "quantity",
            "recipient_type",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)
