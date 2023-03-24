# Django/DRF imports
from django.db import models
from django.contrib.auth.models import User

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from person.models import Patient
from treatment_plan.models import TreatmentPlan
from admission.models import Admission


class PhysicalExamination(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_physical_examination",
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_physical_examination",
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.CASCADE,
        related_name="admission_physical_examination",
    )
    nurses_note = models.ForeignKey(
        NursesNote,
        on_delete=models.PROTECT,
        related_name="nurses_note_physical_examination",
    )
    inspection = models.CharField(max_length=255)
    palpilation = models.CharField(max_length=255)
    auscultation = models.CharField(max_length=255)
    percussion = models.CharField(max_length=255)
    pain_level = models.CharField(max_length=255)
    mental_state = models.CharField(max_length=255)
