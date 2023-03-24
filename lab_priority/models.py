import pytz
from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice, UrgencyTypeChoice, FastingTypeChoice


# Create your models here.
class LabPriority(models.Model):
    urgency = models.CharField(
        max_length=100,
        choices=UrgencyTypeChoice.choices,
        default=UrgencyTypeChoice.NORMAL,
    )
    fasting_status = models.CharField(
        max_length=100,
        choices=FastingTypeChoice.choices,
        default=FastingTypeChoice.NONFASTING,
    )
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )
    created_on = models.DateTimeField(default=now, null=True, blank=True)

    def __str__(self):
        return self.urgency
