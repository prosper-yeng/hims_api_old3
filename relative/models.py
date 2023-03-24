import pytz
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User, Group


# Create your models here.
class Relative(models.Model):
    relative_person = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_relative"
    )
    patient = models.ForeignKey(
        "person.Patient", on_delete=models.CASCADE, related_name="patient_relative"
    )
    relative_type = models.ForeignKey(
        "relative_type.RelativeType",
        on_delete=models.CASCADE,
        related_name="patient_relative_type",
    )
    status = models.ForeignKey(
        "status.Status", on_delete=models.CASCADE, related_name="relative_status"
    )
    created_on = models.DateTimeField(default=now, null=True, blank=True)

    def __str__(self):
        return self.name
