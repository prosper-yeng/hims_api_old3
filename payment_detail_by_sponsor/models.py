from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice
from django.contrib.auth.models import User

from common.views import allowed_extension
from payment.models import Payment
from payment_by_sponsor.models import PaymentBySponsor
from payment_individual.models import PaymentIndividual
from validator.views import validate_file_size


class PaymentDetailBySponsor(models.Model):
    payment = models.ForeignKey(
        PaymentBySponsor,
        on_delete=models.CASCADE,
        related_name="payment_in_PaymentBySponsor_detail",
    )
    instrument_no = models.CharField(max_length=200, null=True, blank=True)
    account_no = models.CharField(max_length=200, null=True, blank=True)
    payer_name = models.CharField(max_length=200, null=True, blank=True)
    post_dated = models.DateTimeField(default=now)
    date_received = models.DateTimeField(default=now)
    instrument_image = models.FileField(
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=allowed_extension),
        ],
        upload_to="instrument_image",
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payment_detail_by_sponsor"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.payer_name)
