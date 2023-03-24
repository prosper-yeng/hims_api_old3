from django.db import models
from django.contrib.auth.models import User

# from medication.models import Medication
# from medication_unit_of_measurement.models import MedicationUnitOfMeasurement
from sponsor_type.models import SponsorType
from status.models import Status
from unit_of_measurement.models import UnitOfMeasurement
from validator.views import valid_phone_number


class Sponsor(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, unique=False)
    sponsor_type = models.ForeignKey(
        SponsorType, on_delete=models.CASCADE, related_name="sponsor_type"
    )
    scheme_code = models.CharField("Scheme Code", max_length=255, blank=True, null=True)
    contact_person = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        unique=False,
    )
    email = models.EmailField(max_length=100, null=False)
    primary_phone = models.CharField(
        validators=[valid_phone_number],
        max_length=15,
        blank=False,
        null=False,
        verbose_name="Primary Phone",
    )
    secondary_phone = models.CharField(
        validators=[valid_phone_number],
        max_length=15,
        verbose_name="Secondary Phone",
        blank=True,
        null=True,
    )
    town = models.ForeignKey(
        "town.Town", on_delete=models.CASCADE, related_name="sponsor_town"
    )
    street = models.CharField(max_length=100, null=False, unique=False)
    post_code = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        unique=False,
        verbose_name="Postcode or Post Box",
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Sponsor_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="status_sponsor"
    )

    def __str__(self):
        return "{}".format(self.name)
