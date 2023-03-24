# Django/DRF imports
from django.db import models
from django.contrib.auth.models import User

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from person.models import Patient
from treatment_plan.models import TreatmentPlan
from admission.models import Admission


class AdditionalData(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_additional_data",
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_additional_data",
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.CASCADE,
        related_name="admission_additional_data",
    )
    nurses_note = models.ForeignKey(
        NursesNote,
        on_delete=models.PROTECT,
        related_name="nurses_note_additional_data",
    )
    diagnostic_data = models.CharField(max_length=255)
    documentation_review = models.CharField(max_length=255)
