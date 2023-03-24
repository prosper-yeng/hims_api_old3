# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from person.models import Patient
from django.contrib.auth.models import User
from admission.models import Admission
from treatment_plan.models import TreatmentPlan
from doctors_note.models import DoctorsNote
from procedure.models import Procedure
from status.models import Status


class ProcedureCare(BaseModel):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="procedure_care_patient"
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.CASCADE,
        related_name="procedure_care_admission",
    )
    nurse = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="nurse_procedure_care"
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.CASCADE,
        related_name="treatment_plan_procedure_care",
    )
    doctor_note = models.ForeignKey(
        DoctorsNote, blank=True, null=True, on_delete=models.CASCADE, related_name="doctor_note_procedure_care"
    )
    procedure = models.ForeignKey(
        Procedure, on_delete=models.CASCADE, related_name="procedure_procedure_care"
    )
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="status_procedure_care"
    )
    date = models.DateTimeField(auto_now=True)
