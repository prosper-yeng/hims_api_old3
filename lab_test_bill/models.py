from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice, UrgencyTypeChoice, FastingTypeChoice
from django.contrib.auth.models import User

from lab_test.models import LabTest

# from transaction.models import Transaction
from warehouse_product.models import WarehouseProduct


class LabTestBill(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="labtest_bill_to_patient"
    )
    # transaction = models.ForeignKey ( Transaction, on_delete=models.CASCADE,  null=True, blank=True, related_name='transaction_in_labtest_bill' )
    lab_test = models.ForeignKey(
        LabTest,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="labtest_in_bill",
    )
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    bill_date = models.DateTimeField(default=now)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="labtest_bill"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.patient)
