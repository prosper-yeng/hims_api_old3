# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from person.models import Patient, Staff
from django.contrib.auth.models import User
from admission.models import Admission
from diagnosis.models import Diagnosis

class TreatmentPlan(BaseModel):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="treatmentplan_patient"
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.CASCADE,
        related_name="treatmentplan_admission",
    )
    objectives = models.TextField(blank=True, null=True)
    estimated_admission_duration = models.CharField(max_length=50)
    treatment_relationale = models.TextField()
    has_accessed_prev_nurses_note = models.BooleanField(default=False)
    patient_condition = models.ForeignKey(
        Diagnosis,
        on_delete=models.CASCADE,
        related_name="patient_condition_treatment_plan",
    )
    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="treatment_plan_doctor",
        null=True,
        blank=True,
    )
