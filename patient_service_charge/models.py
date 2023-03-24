from django.db import models
from django.contrib.auth.models import User

from daily_attendance.models import DailyAttendanceModel
from lab_test.models import LabTest
from medication.models import Medication
from person.models import Patient
from service.models import Service
from currency_type.models import CurrencyType
from sponsor.models import Sponsor
from status.models import Status


class PatientServiceCharge(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    attendance = models.ForeignKey(DailyAttendanceModel, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    price_individual = models.DecimalField(max_digits=10, decimal_places=2)
    price_sponsor = models.DecimalField(max_digits=10, decimal_places=2)
    sponsor = models.ForeignKey(
        Sponsor, on_delete=models.CASCADE, blank=True, null=True
    )
    invoice_id = models.TextField(max_length=10, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    percentage_allowed = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.service)

    class Meta:
        unique_together = (
            "attendance",
            "service",
            "patient",
        )
