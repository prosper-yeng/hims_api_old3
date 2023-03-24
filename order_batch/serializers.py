from rest_framework import serializers

from .models import OrderBatch


class OrderBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBatch
        fields = [
            "id",
            "name",
            "description",
            "batch_number",
            "status",
            "is_deleted",
            "created_by",
        ]

        read_only_fields = ("id",)
