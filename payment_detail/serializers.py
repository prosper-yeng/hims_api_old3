from rest_framework import serializers

from payment_detail.models import PaymentDetail


class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
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
