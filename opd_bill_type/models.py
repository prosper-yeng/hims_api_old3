from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.timezone import now

from choice.views import StatusChoice


class OpdBillType(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    adult_price = models.DecimalField(max_digits=10, decimal_places=2)
    child_price = models.DecimalField(max_digits=10, decimal_places=2)
    adult_discount = models.DecimalField(max_digits=5, decimal_places=2)
    child_discount = models.DecimalField(max_digits=5, decimal_places=2)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="opd_billing_user"
    )
    created_on = models.DateTimeField(default=now)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=StatusChoice.choices)

    def __str__(self):
        return "{}".format(self.name)
