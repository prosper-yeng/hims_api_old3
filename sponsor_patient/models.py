from datetime import datetime
import ipaddress

import django
from django.contrib.auth.models import User
from django.utils.timezone import now


from django.db import models


# Create your models here.
from consulting_room.models import ConsultingRoom
from person.models import Patient
from status.models import Status

# from transaction.models import Transaction


class SponsorPatient(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="patient_sponsor"
    )
    memberId = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="This is the identity number used to identify the patient by the insurance other companies ",
    )
    nhis_serial_no = models.CharField("NHIS Serial Number", max_length=255, blank=True, null=True)
    sponsor = models.ForeignKey(
        "sponsor.Sponsor",
        on_delete=models.CASCADE,
        related_name="sponsor_in_patient",
        null=True,
        blank=True,
    )
    copay_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    bill_limit = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="System User"
    )
    created_on = models.DateTimeField(default=now)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="status_sponsor_patient"
    )
    valid_from = models.DateField(default=now)
    valid_to = models.DateField(default=now)

    def __str__(self):
        return "{}".format(self.patient)
