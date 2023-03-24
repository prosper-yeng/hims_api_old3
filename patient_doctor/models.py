from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from person.models import Patient, Staff


class PatientDoctor(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="patient"
    )
    doctor = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="doctor")
    is_current = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="patient_doctor_user"
    )
    created_on = models.DateTimeField(default=now)
