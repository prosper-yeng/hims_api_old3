from django.db import models
from django.contrib.auth.models import User
from choice.views import StatusChoice


class TransactionLog(models.Model):
    transaction = models.ForeignKey(
        "transaction.Transaction",
        on_delete=models.CASCADE,
    )
    action = models.CharField(max_length=150)
    access_level = models.IntegerField()
    note = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transaction_log_created_by"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.transaction)
