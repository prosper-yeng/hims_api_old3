from datetime import datetime
import ipaddress

import django
from django.contrib.auth.models import User
from django.utils.timezone import now

from attendance_type.models import AttendanceType
from choice.views import StatusChoice, SponsorTypeChoice, visitor_ip_address


from django.db import models


# Create your models here.
from clinic_type.models import ClinicType
from person.models import Patient
from relative.models import Relative
from status.models import Status


class DailyAttendanceModel(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="patient_attendance"
    )
    date_of_visit = models.DateTimeField(default=now)
    OpdNo = models.CharField(max_length=100, blank=True, null=True)
    relative = models.ForeignKey(
        Relative,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="relative",
        verbose_name=" Relative",
    )
    sponsor = models.ForeignKey(
        "sponsor.Sponsor",
        on_delete=models.CASCADE,
        related_name="sponsor",
        null=True,
        blank=True,
    )
    clinic = models.ForeignKey(
        ClinicType, on_delete=models.CASCADE, null=True, blank=True
    )
    attendance_type = models.ForeignKey(
        AttendanceType,
        on_delete=models.CASCADE,
    )
    ccc = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="This is the claims check code field",
    )
    copay = models.IntegerField(default=0)
    vital_sign_taken = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="System User"
    )
    created_on = models.DateTimeField(default=now)
    modified_on = models.DateTimeField(auto_now=True)
    # transaction = models.ForeignKey ( Transaction, on_delete=models.CASCADE, related_name='transaction')
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="status_attendance"
    )

    def __str__(self):
        return "{}".format(self.patient)
