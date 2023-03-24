from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice, DurationUnitChoice
from django.contrib.auth.models import User


from medication.models import Medication
from recipient_type.models import RecipientType


class RecommendedDosage(models.Model):
    medication = models.ForeignKey(
        Medication,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="medication_in_dosage",
    )
    recipient_type = models.ForeignKey(RecipientType, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_of_RecommendedDosage"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.medication)
