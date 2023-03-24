from rest_framework import serializers

from currency_type.serializers import CurrencyTypeSerializer
from procedure.serializers import ProcedureSerializer
from service.serializers import ServiceSerializer
from .models import ProcedureChargeBySponsor


class ProcedureChargeBySponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureChargeBySponsor
        fields = [
            "id",
            "procedure",
            "sponsor",
            "price",
            "currency_type",
            "percentage_allowed",
            "created_by",
            "is_deleted",
            "status",
        ]

        read_only_fields = ("id",)


class CombinedProcedureChargeBySponsorSerializer(serializers.ModelSerializer):
    procedure = ProcedureSerializer(many=False)
    currency_type = CurrencyTypeSerializer(many=False)

    class Meta:
        model = ProcedureChargeBySponsor
        fields = "__all__"
