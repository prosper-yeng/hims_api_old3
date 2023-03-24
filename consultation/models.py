from django.db import models
from django.contrib.auth.models import User, Group

from choice.views import StatusChoice
from daily_attendance.models import DailyAttendanceModel
from diagnosis.models import Diagnosis
from person.models import Patient
from select_unit.models import SelectUnit
from status.models import Status
from vital_sign.models import VitalSign


class Consultation(models.Model):
    # patient = models.ForeignKey ( Patient, on_delete=models.CASCADE, related_name='consult_patient', )
    vital_sign = models.ForeignKey(
        VitalSign,
        on_delete=models.CASCADE,
        related_name="cons_vital",
    )
    # attendance = models.OneToOneField ( DailyAttendanceModel, on_delete=models.CASCADE, related_name='con_daily_attendance', )
    chief_complain = models.TextField(
        max_length=300,
        blank=False,
        null=False,
        help_text="This specifies patient's compliant",
    )

    objective = models.TextField(
        max_length=300, blank=True, null=True, help_text="This specifies doctor's input"
    )
    note = models.TextField(max_length=250, null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="const_created_by"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="cons_status"
    )

    def __str__(self):
        return self.attendance.patient_id
