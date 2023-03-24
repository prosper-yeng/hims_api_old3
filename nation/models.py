import pytz
from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice


# Create your models here.
from status.models import Status


class Nation(models.Model):
    name = models.CharField(
        max_length=100, choices=pytz.country_names.items(), default="GH"
    )
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="nation_status"
    )
    created_on = models.DateTimeField(default=now, null=True, blank=True)

    def __str__(self):
        return self.name
