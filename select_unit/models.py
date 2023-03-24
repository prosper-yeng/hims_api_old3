from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from choice.views import StatusChoice
from status.models import Status


class SelectUnit(models.Model):
    sign = models.CharField(max_length=100, unique=False, null=False, blank=False)
    unit = models.CharField(max_length=100, unique=True, null=False, blank=False)
    measurement_location = models.CharField(
        max_length=100, unique=True, null=True, blank=True
    )
    percentage = models.CharField(max_length=100, unique=True, null=True, blank=True)
    rate = models.CharField(max_length=100, unique=True, null=True, blank=True)
    is_default = models.BooleanField(
        default=True, help_text="Specifies as the default unit of the sign"
    )
    is_min_value = models.IntegerField(
        null=True,
        blank=True,
        help_text="Specifies the minimum value or the measurement",
    )
    is_max_value = models.IntegerField(
        null=True,
        blank=True,
        help_text="Specifies the maximum value or the measurement",
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    created_on = models.DateTimeField(default=now)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def clean(self):
        errors = {}
        if self.is_min_value > self.is_max_value:
            errors[
                "is_min_value"
            ] = "The minimum value cannot be greater than the maximum value."
        if self.is_max_value < self.is_min_value:
            errors[
                "is_max_value"
            ] = "The maximum value cannot be less than the minimum value."
        if errors:
            raise ValidationError(errors)
