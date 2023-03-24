# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from person.models import Patient
from admission.models import Admission
from ward.models import Ward
from consultation_diagnosis.models import ConsultationDiagnosis


class IntraHospitalPatientTransfer(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_intra_hospital_patient_transfer",
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.CASCADE,
        related_name="intrahosppatienttrans_admission",
    )
    source = models.ForeignKey(
        Ward,
        on_delete=models.CASCADE,
        related_name="intra_hospital_patient_transfer_source",
        blank=True,
        null=True,
    )
    destination = models.ForeignKey(
        Ward,
        on_delete=models.CASCADE,
        related_name="intra_hospital_patient_transfer_destination",
        blank=True,
        null=True,
    )
    reason = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # TODO: Test and remove try, except 
        try:
            # Change the ward in admission to be in line with admission award
            Admission.objects.filter(id=self.admission.id).update(ward__id=self.destination.id)
        except:
            pass
        super().save(*args, **kwargs)
