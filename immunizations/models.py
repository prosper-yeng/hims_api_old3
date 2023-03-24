# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from diagnosis.models import Diagnosis
from person.models import Patient
from treatment_plan.models import TreatmentPlan
from admission.models import Admission


class Immunizations(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_immunizations",
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_immunizations",
    )

    nurses_note = models.ForeignKey(
        NursesNote, 
        on_delete=models.CASCADE, 
        related_name="nurses_note_immunizations"
    )
    date = models.DateTimeField(auto_now=True)
    disease = models.ForeignKey(
        Diagnosis, 
        on_delete=models.CASCADE, 
        related_name="disease_immunizations"
    )
    certificate = models.CharField(max_length=255)
   
