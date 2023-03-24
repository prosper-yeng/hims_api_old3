# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from treatment_plan.models import TreatmentPlan

class PatientSpecificGoal(BaseModel):
    nurses_note = models.ForeignKey(
        NursesNote, 
        on_delete=models.CASCADE, 
        related_name="patient_specific_goal_nurses_note"
    )
    goal = models.CharField(max_length=255)
    potential_outcome = models.CharField(max_length=255)
    intervention = models.CharField(max_length=255)
    current_need = models.CharField(max_length=255)
    potential_harm = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_patient_specific_goal",
    )
