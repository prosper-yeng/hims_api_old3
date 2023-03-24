# Django/DRF imports
from django.db import models
from django.contrib.auth.models import User

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from person.models import Patient
from treatment_plan.models import TreatmentPlan
from admission.models import Admission

class NeedType(BaseModel):

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_needtype",
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_needtype",
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.CASCADE,
        related_name="admission_needtype",
    )
    name = models.CharField(max_length=255)
