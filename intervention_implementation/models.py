# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from intervention_type.models import InterventionType
from patient_specific_goal.models import PatientSpecificGoal


class InterventionImplementation(BaseModel):
    nurses_note = models.ForeignKey(
        NursesNote, 
        on_delete=models.CASCADE, 
        related_name="nurses_note_intervention_implementation"
    )
    intervention_type = models.ForeignKey(
        InterventionType, 
        on_delete=models.CASCADE, 
        related_name="inteventation_type_intervention_implementation"
    )
    patient_specific_goal = models.ForeignKey(
        PatientSpecificGoal, 
        on_delete=models.CASCADE, 
        related_name="patient_specific_goal_intervention_implementation"
    )
    details = models.TextField()