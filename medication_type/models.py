from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User


class MedicationType(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="prescriber"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.name)
