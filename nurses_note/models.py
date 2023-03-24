# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from person.models import Patient, Staff
from admission.models import Admission
from treatment_plan.models import TreatmentPlan
from django.contrib.auth.models import User


class NursesNote(BaseModel):
    patient = models.ForeignKey(
        Patient, on_delete=models.PROTECT, related_name="nurses_note_patient"
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.PROTECT,
        related_name="nurses_note_admission",
    )
    nurse = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="nurses_note_nurse"
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.PROTECT,
        related_name="treatment_plan_nurses_note",
    )
