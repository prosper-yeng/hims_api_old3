# Django/DRF imports
from django.db import models
from django.contrib.auth.models import User

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from person.models import Patient
from treatment_plan.models import TreatmentPlan
from admission.models import Admission


class FamilyHistory(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_family_history",
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_family_history",
    )

    nurses_note = models.ForeignKey(
        NursesNote,
        on_delete=models.CASCADE,
        related_name="nurses_note_family_history",
    )
    family_disease = models.CharField(max_length=255)
    brief_history = models.TextField()
    
