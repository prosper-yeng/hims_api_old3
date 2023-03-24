from django.db import models
from django.contrib.auth.models import User, Group

from consultation_diagnosis.models import ConsultationDiagnosis
from daily_attendance.models import DailyAttendanceModel

from procedure.models import Procedure
from select_unit.models import SelectUnit
from sponsor.models import Sponsor
from status.models import Status


class DiagnosedProcedure(models.Model):
    consultation_diagnosis = models.ForeignKey(
        ConsultationDiagnosis,
        on_delete=models.CASCADE,
        related_name="cons_diag_procedure",
    )
    # attendance= models.ForeignKey (DailyAttendanceModel, on_delete=models.CASCADE, related_name='cons_procedure_transaction', )
    procedure = models.ForeignKey(
        Procedure,
        on_delete=models.CASCADE,
        related_name="cons_diag_procedure",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.CASCADE,
        related_name="cons_diag_sponsor",
        null=True,
        blank=True,
    )
    note = models.TextField(max_length=250, null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="const_procedure_created_by"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="cons_proceudre_status"
    )

    def __str__(self):
        return self.procedure.name
