from rest_framework import serializers

from payment_detail.models import PaymentDetail
from payment_detail_Individual.models import PaymentDetailIndividual
from payment_individual.serializers import PaymentIndividualSerializer


class PaymentDetailIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetailIndividual
        fields = [
            "id",
            "payment",
            "instrument_no",
            "account_no",
            "payer_name",
            "instrument_image",
            "post_dated",
            "date_received",
            "status",
            "created_by",
        ]
        read_only_fields = ("id",)


class CombinedPaymentDetailSerializer(serializers.ModelSerializer):
    payment = PaymentIndividualSerializer(many=False)

    class Meta:
        model = PaymentDetailIndividual
        fields = "__all__"
