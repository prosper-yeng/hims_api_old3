from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice
from district.models import District

# Create your models here.
from district.models import District
from status.models import Status


class Town(models.Model):
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="town_district"
    )
    name = models.CharField(max_length=100, null=False, unique=True)
    created_on = models.DateTimeField(default=now)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="town_status"
    )

    def __str__(self):
        return self.name
