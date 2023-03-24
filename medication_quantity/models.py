from django.db import models

import quantity_unit_type.models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from medication.models import Medication
from medication_unit_of_measurement.models import MedicationUnitOfMeasurement
from supplier.models import Supplier
from unit_of_measurement.models import UnitOfMeasurement


class MedicationQuantity(models.Model):
    medication = models.ForeignKey(
        Medication,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="medication_with_quantity",
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="supplier_with_quantity",
    )
    unit_type = models.ForeignKey(
        "quantity_unit_type.QuantityUnitType",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="quantity_unit",
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    note = models.TextField(max_length=200, null=True, blank=True, unique=False)
    batch_no = models.TextField(max_length=200, null=True, blank=True, unique=False)
    expiry_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medication_quantity_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.batch_no)
