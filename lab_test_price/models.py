from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

# from client.models import Client
from lab_test.models import LabTest
from sponsor.models import Sponsor
from status.models import Status


class LabTestPrice(models.Model):
    lab_test = models.ForeignKey(
        LabTest,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="lab_test_with_price",
    )
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    profit_margin = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vat = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other_tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lab_test_price_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="lab_test_with_status"
    )

    def price(self):
        selling_price = (
            self.cost_price
            + (self.cost_price * self.profit_margin)
            + (self.cost_price * self.vat)
            + (self.cost_price * self.other_tax)
        )
        selling_price = selling_price - (selling_price * self.discount)

        return selling_price
