from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from daily_attendance.models import DailyAttendanceModel
from procedure.models import Procedure
from procedure_charge.models import ProcedureCharge
from procedure_charge_by_sponsor.models import ProcedureChargeBySponsor
from service.models import Service
from currency_type.models import CurrencyType
from sponsor.models import Sponsor
from status.models import Status


class ProcedureSchedule(models.Model):
    procedure_charge_by_sponsor = models.ForeignKey(
        ProcedureChargeBySponsor, on_delete=models.CASCADE, null=True, blank=True
    )
    procedure_charge = models.ForeignKey(
        ProcedureCharge, on_delete=models.CASCADE, null=True, blank=True
    )
    schedule_date = models.DateTimeField()
    attendance = models.ForeignKey(DailyAttendanceModel, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.attendance.patient)
