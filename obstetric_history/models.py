# Django/DRF imports
from django.db import models
from django.contrib.auth.models import User

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from person.models import Patient
from treatment_plan.models import TreatmentPlan
from admission.models import Admission


class ObstetricHistory(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_obstetric_history",
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_obstetric_history",
    )

    nurses_note = models.ForeignKey(
        NursesNote,
        on_delete=models.PROTECT,
        related_name="nurses_note_obstetric_history",
    )
    complication = models.CharField(max_length=255)
    pregnancy_outcome = models.CharField(max_length=255)
    abnormality = models.CharField(max_length=255)
    abnormality_assessment = models.CharField(max_length=255)
    assessment_type = models.CharField(max_length=255)
    size_of_wound = models.CharField(max_length=255)

