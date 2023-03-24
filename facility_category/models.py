import pytz
from django.db import models
from django.utils.timezone import now


# Create your models here.
class FacilityCategory(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    status = models.ForeignKey(
        "status.Status", on_delete=models.CASCADE, related_name="facility_cat_status"
    )
    created_on = models.DateTimeField(default=now, null=True, blank=True)

    def __str__(self):
        return self.name
