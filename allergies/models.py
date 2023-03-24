import pytz
from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice


# Create your models here.
from nurses_note.models import NursesNote


class Allergies(models.Model):
    patient = models.ForeignKey(
        "person.Patient", on_delete=models.CASCADE, related_name="patient_allergies"
    )

    nurses_note = models.ForeignKey (
        NursesNote,
        on_delete=models.CASCADE, null=True, blank=True,
        related_name="nurses_note_allergies"
    )
    name = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField(max_length=100, null=False, unique=True)
    status = models.ForeignKey(
        "status.Status", on_delete=models.CASCADE, related_name="allergies_status"
    )
    created_on = models.DateTimeField(default=now, null=True, blank=True)

    def __str__(self):
        return self.name
