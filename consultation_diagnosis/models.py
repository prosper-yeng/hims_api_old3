from django.db import models
from django.contrib.auth.models import User, Group

from consultation.models import Consultation
from daily_attendance.models import DailyAttendanceModel
from diagnosis.models import Diagnosis
from person.models import Patient
from select_unit.models import SelectUnit
from status.models import Status
from vital_sign.models import VitalSign
from patient_type.models import PatientType


class ConsultationDiagnosis(models.Model):
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.CASCADE,
        related_name="cons_diag_vital",
    )
    patient_type = models.ForeignKey(
        PatientType,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="patient_type_consultation_diagnosis",
    )
    vital_sign = models.ForeignKey(
        VitalSign,
        on_delete=models.CASCADE,
        related_name="vital_sign_in_cons_diag",
    )

    diagnosis = models.ForeignKey(
        Diagnosis,
        on_delete=models.CASCADE,
        related_name="cons_diag",
    )
    note = models.TextField(max_length=250, null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="const_diag_created_by"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="cons_diag_status"
    )
    is_confirmed = models.BooleanField(default=False)
    ipd = models.BooleanField(default=False)

    def __str__(self):
        return self.vital_sign

    class Meta:
        unique_together = ("vital_sign", "consultation", "diagnosis")
