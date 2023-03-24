from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from client.models import Client
from client_type.models import ClientType
from insurance_type.models import InsuranceType
from medication.models import Medication
from medication_unit_of_measurement.models import MedicationUnitOfMeasurement
from sponsor.models import Sponsor
from status.models import Status
from unit_of_measurement.models import UnitOfMeasurement


class MedicationPrice(models.Model):
    medication = models.ForeignKey(
        Medication, on_delete=models.CASCADE, related_name="medication_with_price"
    )
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="client_type_for_medication_price",
    )
    selling_unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medication_price_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="medication_status"
    )

    def __str__(self):
        return "{}".format(self.selling_unit_price)

    class Meta:
        unique_together = ("medication", "sponsor")
