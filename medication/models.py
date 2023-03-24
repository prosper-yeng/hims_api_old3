from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from daily_attendance.models import DailyAttendanceModel
from medication_type.models import MedicationType
from person.models import Patient
from prescription.models import Prescription
from sponsor.models import Sponsor
from status.models import Status
from unit_of_measurement.models import UnitOfMeasurement
from warehouse_product.models import WarehouseProduct


class Medication(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="medication_patient",
    )
    attendance = models.ForeignKey(
        DailyAttendanceModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="attendancein_medication",
    )
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="medication_sponsor",
    )
    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="medication_type_in_medication",
    )
    product = models.ForeignKey(
        WarehouseProduct, on_delete=models.CASCADE, related_name="warehouse_medication"
    )
    remark = models.TextField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="medication_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="medication_record_status"
    )

    def __str__(self):
        return "{}".format(self.patient)
