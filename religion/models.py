import pytz
from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice


# Create your models here.
class Religion(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    status = models.ForeignKey(
        "status.Status", on_delete=models.CASCADE, related_name="Religion"
    )

    created_on = models.DateTimeField(default=now, null=True, blank=True)

    def __str__(self):
        return self.name
