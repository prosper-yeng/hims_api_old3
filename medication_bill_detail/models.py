from django.db import models
from choice.views import StatusChoice, UrgencyTypeChoice, FastingTypeChoice
from django.contrib.auth.models import User
from medication_bill.models import MedicationBill


from medication.models import Medication


class MedicationBillDetail(models.Model):
    medication_bill = models.ForeignKey(
        MedicationBill, on_delete=models.CASCADE, related_name="medication_bill_id"
    )
    medication = models.ForeignKey(
        Medication,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="medication_bill_detail",
    )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, default=0, decimal_places=2)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medication_bill_detail_create"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.medication)
