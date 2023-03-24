from django.db import models

import quantity_unit_type.models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from medication.models import Medication

from supplier.models import Supplier


class MedicationOrder(models.Model):
    medication = models.ForeignKey(
        Medication,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="medication_order",
    )

    order_quantity_unit = models.ForeignKey(
        "quantity_unit_type.QuantityUnitType",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="order_unit",
    )
    order_quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)

    selling_quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    selling_quantity_unit = models.ForeignKey(
        "quantity_unit_type.QuantityUnitType",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="selling_unit",
    )
    expiry_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medication_order_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.medication)
