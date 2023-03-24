from rest_framework import serializers

from currency_type.serializers import CurrencyTypeSerializer
from procedure.serializers import ProcedureSerializer
from service.serializers import ServiceSerializer
from .models import ProcedureCharge


class ProcedureChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureCharge
        fields = [
            "id",
            "procedure",
            "price",
            "currency_type",
            "created_by",
            "is_deleted",
            "status",
        ]

        read_only_fields = ("id",)


class CombinedProcedureChargeSerializer(serializers.ModelSerializer):
    procedure = ProcedureSerializer(many=False)
    currency_type = CurrencyTypeSerializer(many=False)

    class Meta:
        model = ProcedureCharge
        fields = "__all__"
