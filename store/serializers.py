from rest_framework import serializers

from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    warehouse_name = serializers.CharField(source="warehouse.name", required=False)

    class Meta:
        model = Store
        fields = [
            "id",
            "name",
            "description",
            "warehouse",
            "warehouse_name",
            "is_deleted",
            "status",
            "created_by",
        ]

        read_only_fields = ("id",)
