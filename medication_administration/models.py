# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from person.models import Patient
from django.contrib.auth.models import User 
from admission.models import Admission
from treatment_plan.models import TreatmentPlan


class MedicationAdministration(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="medication_administration_patient",
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.PROTECT,
        related_name="medication_administration_admission",
    )
    medication_on = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    nurse = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="medication_administration_nurse"
    )
    treatment_plan = models.ForeignKey(
        TreatmentPlan,
        on_delete=models.PROTECT,
        related_name=
        "treatment_plan_medication_administration",
    )
    date = models.DateTimeField(auto_now=True)
    
