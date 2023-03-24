from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice, UrgencyTypeChoice, FastingTypeChoice
from django.contrib.auth.models import User
from insurance_type.models import InsuranceType

from medication.models import Medication
from prescription.models import Prescription
from warehouse_product.models import WarehouseProduct


class MedicationBill(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medication_bill_to_patient"
    )
    # transaction = models.ForeignKey ( Transaction, on_delete=models.CASCADE,  null=True, blank=True, related_name='transaction_in_medication_bill' )
    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="prescription_in_medication_bill",
    )
    product = models.ForeignKey(
        WarehouseProduct,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="warehouse_product_in_medication_bill",
    )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    bill_date = models.DateTimeField(default=now)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medication_bill"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.patient)
