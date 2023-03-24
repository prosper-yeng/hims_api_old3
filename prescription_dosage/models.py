from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice, DurationUnitChoice
from django.contrib.auth.models import User


from medication.models import Medication
from medication_dosage.models import MedicationDosage
from prescription.models import Prescription


class PrescriptionDosage(models.Model):
    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="prescription_with_dosage",
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    time = models.CharField(max_length=100, unique=False, null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_of_PrescriptionDosage"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.prescription)
