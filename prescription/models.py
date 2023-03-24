from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice, DurationUnitChoice
from django.contrib.auth.models import User

from consultation_diagnosis.models import ConsultationDiagnosis
from daily_attendance.models import DailyAttendanceModel

# from medication.models import Medication
from medication_dosage.models import MedicationDosage
from person.models import Patient
from sponsor.models import Sponsor
from status.models import Status
from warehouse_product.models import WarehouseProduct


class Prescription(models.Model):
    consultation_diagnosis = models.ForeignKey(
        ConsultationDiagnosis, on_delete=models.CASCADE, related_name="prescribed_to"
    )
    warehouse_product = models.ForeignKey(
        WarehouseProduct, on_delete=models.CASCADE, related_name="prescribed_medicine"
    )
    # patient = models.ForeignKey ( Patient, on_delete=models.CASCADE, related_name='patient_medicine' )
    # attendance = models.ForeignKey ( DailyAttendanceModel, on_delete=models.CASCADE,related_name='attendance_prescription' )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.CASCADE,
        related_name="sponsor_prescription",
        null=True,
        blank=True,
    )

    quantity = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    duration = models.IntegerField(default=0)
    duration_unit = models.CharField(
        max_length=100,
        choices=DurationUnitChoice.choices,
        default=DurationUnitChoice.DAY,
    )
    prescription_date = models.DateTimeField(default=now)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="prescribed_by"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="prescribed_status"
    )

    def __str__(self):
        return "{}".format(self.warehouse_product.name)
