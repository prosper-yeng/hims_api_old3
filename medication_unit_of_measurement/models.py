from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

# from medication.models import Medication
from unit_of_measurement.models import UnitOfMeasurement


class MedicationUnitOfMeasurement(models.Model):
    # medication=models.ForeignKey(Medication,on_delete=models.CASCADE , null=True, blank=True, related_name='medication_with_unit')
    unit_of_measurement = models.ForeignKey(
        UnitOfMeasurement,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="unit_of_measurement_with_medication",
    )
    selling_unit = models.BooleanField()
    brand = models.TextField(max_length=100, null=True, blank=True, unique=True)
    description = models.TextField(max_length=100, null=True, blank=True, unique=False)
    bar_code = models.TextField(max_length=200, null=True, blank=True, unique=False)
    drug_code = models.TextField(max_length=100, null=True, blank=True, unique=False)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="medication_unit_of_measurement_user",
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    NHIS_list = models.BooleanField(default=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.selling_unit)
