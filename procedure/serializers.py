from rest_framework import serializers

from .models import Procedure


class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = [
            "id",
            "name",
            "gdrg",
            "icd_code",
            "description",
            "status",
            "created_by",
        ]

        read_only_fields = ("id",)
