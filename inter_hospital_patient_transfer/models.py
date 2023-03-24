# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from person.models import Patient
from admission.models import Admission
from facility.models import Facility
from consultation_diagnosis.models import ConsultationDiagnosis

class InterHospitalPatientTransfer(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="patient_inter_hospital_patient_transfer",
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.CASCADE,
        related_name="interhosppatienttrans_admission",
    )
    source = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        related_name="inter_hospital_patient_transfer_source",
        blank=True,
        null=True,
    )
    destination = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        related_name="inter_hospital_patient_transfer_destination",
        blank=True,
        null=True,
    )
    reason = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
