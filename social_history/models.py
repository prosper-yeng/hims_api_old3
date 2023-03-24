# Django/DRF imports
from django.db import models
from django.contrib.auth.models import User

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from marital_status.models import MaritalStatus
from occupation.models import Occupation
from habit.models import Habit
from person.models import Patient
from treatment_plan.models import TreatmentPlan
from admission.models import Admission


class SocialHistory(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_social_history",
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_social_history",
    )

    nurses_note = models.ForeignKey(
        NursesNote,
        on_delete=models.CASCADE,
        related_name="nurses_note_social_history",
    )
    marital_status = models.ForeignKey(
        MaritalStatus,
        on_delete=models.PROTECT,
        related_name="marital_status_social_history",
    )
    occupation = models.ForeignKey(
        Occupation,
        on_delete=models.PROTECT,
        related_name="occupation_social_history",
    )
    habit = models.ForeignKey(
        Habit,
        on_delete=models.PROTECT,
        related_name="occupation_social_history",
    )
    family_situation = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    sexual_history = models.CharField(max_length=255)

    
