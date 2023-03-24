# Django/DRF imports
from django.db import models
from django.contrib.auth.models import User

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote

class SubjectiveInfo(BaseModel):
    nurses_note = models.ForeignKey(
        NursesNote,
        on_delete=models.PROTECT,
        related_name="nurses_note_subjective_info",
    )
    personal_feeling = models.CharField(max_length=255)
    personal_thought = models.CharField(max_length=255)
