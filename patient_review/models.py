# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from person.models import Patient, Staff
from admission.models import Admission
from diagnosis.models import Diagnosis
from treatment_plan.models import TreatmentPlan
from doctors_note.models import DoctorsNote
from procedure.models import Procedure
from status.models import Status


class PatientReview(BaseModel):
    patient = models.ForeignKey(
        Patient, on_delete=models.PROTECT, related_name="patient_review_patient"
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.PROTECT,
        related_name="patient_review_admission",
    )
    doctor = models.ForeignKey(
        Staff, on_delete=models.PROTECT, related_name="patient_review_doctor"
    )
    reason = models.TextField()
    # TODO: patient_type
    diagnosis = models.ForeignKey(
        Diagnosis, on_delete=models.PROTECT, related_name="patient_review_diagnosis"
    )
