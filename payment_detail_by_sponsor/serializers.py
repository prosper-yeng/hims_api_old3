from rest_framework import serializers

from payment_detail.models import PaymentDetail
from payment_detail_Individual.models import PaymentDetailIndividual
from payment_detail_by_sponsor.models import PaymentDetailBySponsor
from payment_individual.serializers import PaymentIndividualSerializer


class PaymentDetailBySponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetailBySponsor
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
    payment = PaymentDetailBySponsorSerializer(many=False)

    class Meta:
        model = PaymentDetailBySponsor
        fields = "__all__"
