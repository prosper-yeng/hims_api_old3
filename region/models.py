from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice
from nation.models import Nation


# Create your models here.
from status.models import Status


class Region(models.Model):
    nation = models.ForeignKey(
        "nation.Nation", on_delete=models.CASCADE, related_name="nation"
    )
    name = models.CharField(max_length=100, null=False, unique=True)
    regional_code = models.CharField(max_length=50, null=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="region_status"
    )

    def __str__(self):
        return self.name
