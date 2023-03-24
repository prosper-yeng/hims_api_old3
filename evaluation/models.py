# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from patient_specific_goal.models import PatientSpecificGoal
from intervention_implementation.models import InterventionImplementation
from treatment_plan.models import  TreatmentPlan


class Evaluation(BaseModel):
    nurses_note = models.ForeignKey(
        NursesNote, 
        on_delete=models.CASCADE, 
        related_name="nurses_note_evaluation"
    )
    rating = models.CharField(max_length=255)
    reassessment_detail = models.TextField()
    intervention_implementation = models.ForeignKey(
        InterventionImplementation, 
        on_delete=models.CASCADE,
        blank=True, null=True, 
        related_name="intervention_implementation_evaluation"
    )
    patient_specific_goal = models.ForeignKey(
        PatientSpecificGoal, 
        on_delete=models.CASCADE,
        blank=True, null=True, 
        related_name="patient_specific_goal_evaluation"
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan, 
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        related_name="treatment_plan_evaluation"
    )
    condition_reassessment = models.BooleanField(default=False)