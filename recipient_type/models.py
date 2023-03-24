from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice
from django.contrib.auth.models import User


class RecipientType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="prescription_dosage"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.name)
