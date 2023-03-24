# Django/DRF imports
from django.db import models
from django.contrib.auth.models import User

# Local app imports
from hims_api.basemodel import BaseModel
from nurses_note.models import NursesNote
from need_type.models import NeedType
from person.models import Patient
from treatment_plan.models import TreatmentPlan
from admission.models import Admission

class PatientNeeds(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_patient_needs",
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_patient_needs",
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.CASCADE,
        related_name="admission_patient_needs",
    )
    nurses_note = models.ForeignKey(
        NursesNote,
        on_delete=models.CASCADE,
        related_name="nurses_note_patient_needs",
    )
    need_type = models.ForeignKey(
        NeedType,
        on_delete=models.CASCADE,
        related_name="need_type_patient_needs",
    )
    comment = models.TextField()
