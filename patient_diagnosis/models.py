# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from diagnosis.models import Diagnosis
from treatment_plan.models import TreatmentPlan

class PatientDiagnosis(BaseModel):
    nurses_note = models.ForeignKey(
        NursesNote, 
        on_delete=models.CASCADE, 
        related_name="patient_diagnosis_nurses_note"
    )
    diagnosis = models.ForeignKey(
        Diagnosis,
        on_delete=models.CASCADE,
        related_name="diagnosis_patient_diagnosis",
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_patient_diagnosis",
    )
