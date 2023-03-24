from django.db import models
from django.contrib.auth.models import User

from status.models import Status


class ClinicType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    specialty_code = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="specialty_code"
    )
    specialty_description = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="description"
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)
