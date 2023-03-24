from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from medication.models import Medication
from medication_unit_of_measurement.models import MedicationUnitOfMeasurement
from unit_of_measurement.models import UnitOfMeasurement
from validator.views import valid_phone_number


class Client(models.Model):
    name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        unique=False,
    )
    client_type = models.ForeignKey(
        "client_type.ClientType", on_delete=models.CASCADE, related_name="client_type"
    )
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
        blank=True,
        null=True,
        verbose_name="Primary Phone",
    )
    secondary_phone = models.CharField(
        validators=[valid_phone_number],
        max_length=15,
        verbose_name="Secondary Phone",
        blank=True,
        null=True,
    )

    country = models.ForeignKey(
        "nation.Nation", on_delete=models.CASCADE, related_name="client_country"
    )
    region = models.ForeignKey(
        "region.Region",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="client_region",
    )
    district = models.ForeignKey(
        "district.District", on_delete=models.CASCADE, related_name="client_district"
    )
    town = models.ForeignKey(
        "town.Town", on_delete=models.CASCADE, related_name="client_town"
    )
    street = models.CharField(max_length=100, null=False, unique=False)
    post_code = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        unique=False,
        verbose_name="Postcode or Post Box",
    )
    discount_allowed = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="client_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100, choices=StatusChoice.choices, default=StatusChoice.ACTIVE
    )

    def __str__(self):
        return "{}".format(self.name)
