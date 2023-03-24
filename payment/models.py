from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice, UrgencyTypeChoice, FastingTypeChoice
from django.contrib.auth.models import User

from client.models import Client
from client_type.models import ClientType
from company.models import Company
from mode_of_payment.models import ModeOfPayment
from person.models import Patient
from service_type.models import ServiceType
from sponsor.models import Sponsor
from status.models import Status

# from transaction.models import Transaction


class Payment(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="payment_to_patient"
    )
    # transaction = models.ForeignKey ( Transaction, on_delete=models.CASCADE, related_name='transaction_in_payment' )
    mop = models.ForeignKey(
        ModeOfPayment, on_delete=models.CASCADE, related_name="mop_in_payment"
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="company_in_payment"
    )
    sponsor = models.ForeignKey(
        Sponsor, on_delete=models.CASCADE, related_name="sponsor_type_in_payment"
    )
    service_type = models.ForeignKey(
        ServiceType, on_delete=models.CASCADE, related_name="service_type_in_payment"
    )
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=now)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="payment_status"
    )
    remark = models.CharField(max_length=200, null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payment"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.patient)
