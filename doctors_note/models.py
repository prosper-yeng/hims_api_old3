# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from person.models import Patient, Staff
from django.contrib.auth.models import User
from admission.models import Admission
from treatment_plan.models import TreatmentPlan


class DoctorsNote(BaseModel):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="doctors_note_patient"
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.CASCADE,
        related_name="doctors_note_admission",
    )
    note = models.TextField(blank=True, null=True)
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="doctors_note_doctor"
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="doctors_note_treatment_plan",
    )
