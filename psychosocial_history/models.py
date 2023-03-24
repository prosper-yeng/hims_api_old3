# Django/DRF imports
from django.db import models
from django.contrib.auth.models import User

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from occupation.models import Occupation
from habit.models import Habit
from person.models import Patient
from treatment_plan.models import TreatmentPlan
from admission.models import Admission


class PsychosocialHistory(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_psychosocial_history",
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_psychosocial_history",
    )

    nurses_note = models.ForeignKey(
        NursesNote,
        on_delete=models.CASCADE,
        related_name="nurses_note_psychosocial_history",
    )
    mental_health = models.CharField(max_length=255)
    psychological_health = models.CharField(max_length=255)
    behavorial_health = models.CharField(max_length=255)

