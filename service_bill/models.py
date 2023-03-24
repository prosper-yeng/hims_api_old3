from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User
from service.models import Service
from currency_type.models import CurrencyType

# from transaction.models import Transaction


class ServiceBill(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    # transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    amount = models.FloatField()
    currency_type = models.ForeignKey(CurrencyType, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.service)
