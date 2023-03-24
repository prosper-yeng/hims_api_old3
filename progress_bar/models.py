from django.db import models
from django.contrib.auth.models import User

from daily_attendance.models import DailyAttendanceModel
from service.models import Service
from status.models import Status


class ProgressBar(models.Model):
    attendance = models.OneToOneField(
        DailyAttendanceModel, on_delete=models.CASCADE, unique=True
    )
    # service=models.ForeignKey(Service,on_delete=models.CASCADE, related_name='service_progress')
    vital_sign = models.BooleanField(default=False)
    consultation = models.BooleanField(default=False)
    diagnosis = models.BooleanField(default=False)
    lab = models.BooleanField(default=False)
    procedure = models.BooleanField(default=False)
    prescription = models.BooleanField(default=False)
    medication = models.BooleanField(default=False)
    registration_fee = models.BooleanField(default=False)
    consultation_fee = models.BooleanField(default=False)
    procedure_fee = models.BooleanField(default=False)
    lab_bill = models.BooleanField(default=False)
    medication_bill = models.BooleanField(default=False)
    end_process = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="progress_bar_created_by"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="progress_status"
    )

    def __str__(self):
        return "{}".format(self.attendance)
