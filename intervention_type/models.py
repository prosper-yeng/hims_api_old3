# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote

class InterventionType(BaseModel):
    # nurses_note = models.ForeignKey(
    #     NursesNote, 
    #     on_delete=models.CASCADE, 
    #     related_name="nurses_note_intervention_type"
    # )
    name = models.CharField(max_length=255)