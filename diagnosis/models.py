from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from status.models import Status


class Diagnosis(models.Model):
    name = models.TextField(max_length=100, null=False, unique=True)
    description = models.TextField(max_length=100, null=True, blank=True, unique=False)
    gdrg = models.TextField(max_length=200, null=True, blank=True, unique=False)
    icd_code = models.TextField(max_length=100, null=True, blank=True, unique=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="diagnosis_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="diagnosis_user"
    )

    def __str__(self):
        return "{}".format(self.name)
