from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from lab_test_type.models import LabTestType


class LabTest(models.Model):
    lab_test_type = models.ForeignKey(
        LabTestType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="lab_test",
    )
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    description = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    icd = models.CharField(max_length=100, null=True, blank=True, unique=True)
    drg = models.CharField(max_length=100, null=True, blank=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lab_test_creator"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey ("status.Status", on_delete=models.CASCADE, related_name="lab_test_status")

    def __str__(self):
        return "{}".format(self.name)
