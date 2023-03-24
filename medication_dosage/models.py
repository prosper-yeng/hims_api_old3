from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from medication_unit_of_measurement.models import MedicationUnitOfMeasurement
from dosage_type.models import DosageType


class MedicationDosage(models.Model):
    medication_unit_of_measurement = models.ForeignKey(
        MedicationUnitOfMeasurement,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="medication_unit_of_measurement_with_dosage",
    )
    dosage_type = models.ForeignKey(
        DosageType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="medication_dosage",
    )
    recommended_dosage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medication_dosage_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.recommended_dosage)
