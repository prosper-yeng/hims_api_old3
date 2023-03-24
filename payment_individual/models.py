from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice, UrgencyTypeChoice, FastingTypeChoice
from django.contrib.auth.models import User


from company.models import Company
from daily_attendance.models import DailyAttendanceModel
from mode_of_payment.models import ModeOfPayment
from patient_service_charge.models import PatientServiceCharge
from person.models import Patient
from sponsor.models import Sponsor

from status.models import Status


class PaymentIndividual(models.Model):
    patient_service_charge = models.ForeignKey(
        PatientServiceCharge, on_delete=models.CASCADE, related_name="payment_of_patient_service_charge"
    )
    '''attendance = models.ForeignKey(
        DailyAttendanceModel,
        on_delete=models.CASCADE,
        related_name="attendacne_inindividual_payment",
    )
    '''
    mop = models.ForeignKey(
        ModeOfPayment,
        on_delete=models.CASCADE,
        related_name="mop_in_individual_payment",
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="company_in_individual_payment",
    )
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sponsor_type_in_individual_payment",
    )

    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=now)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="payment_individual_status"
    )
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="payment_individual"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.patient)
