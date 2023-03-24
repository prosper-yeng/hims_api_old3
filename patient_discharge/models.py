# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from person.models import Patient, Staff
from admission.models import Admission

from bed_allocation.models import BedAllocation


class PatientDischarge(BaseModel):
    patient = models.ForeignKey(
        Patient, on_delete=models.PROTECT, related_name="patient_discharge_patient"
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.PROTECT,
        related_name="patient_discharge_admission",
    )
    doctor = models.ForeignKey(
        Staff, on_delete=models.PROTECT, related_name="patient_discharge_doctor"
    )
    reason = models.TextField()
    treatment_outcome = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        bed_allocation = BedAllocation.objects.filter(
            is_active=False,
            admission__consultation_diagnosis__consultation__vital_sign__attendance__patient__id=self.patient.id,
        ).first()
        if bed_allocation:
            bed_allocation.deallocated_date = self.created_at
            bed_allocation.is_active = True
            bed_allocation.save()
        super().save(*args, **kwargs)
