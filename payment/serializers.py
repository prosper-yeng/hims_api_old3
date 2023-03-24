from rest_framework import serializers

from person.serializers import UserSerializer, PatientSerializer
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source="company.name", required=False)
    service_type_name = serializers.CharField(
        source="service_type.name", required=False
    )

    class Meta:
        model = Payment
        fields = [
            "id",
            "patient",
            # 'transaction',
            "mop",
            "company",
            "company_name",
            "sponsor",
            "service_type",
            "service_type_name",
            "amount_paid",
            "payment_date",
            "remark",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)


class CombinedPaymentPatientUserSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)
    patient = PatientSerializer(many=False)

    class Meta:
        model = Payment
        fields = "__all__"
