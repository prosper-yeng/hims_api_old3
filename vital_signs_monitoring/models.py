# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from person.models import Patient, Staff
from admission.models import Admission
from vital_sign.models import VitalSign


class VitalSignsMonitoring(BaseModel):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="vital_signs_monitoring_patient"
    )
    admission = models.ForeignKey(
        Admission,
        on_delete=models.CASCADE,
        related_name="vital_signs_monitoring_admission",
    )
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="staff_vital_signs_monitoring"
    )
    vital_sign = models.ForeignKey(
        VitalSign,
        on_delete=models.SET_NULL,
        null=True,
        related_name="vital_sign_vital_sign_monitoring",
    )
