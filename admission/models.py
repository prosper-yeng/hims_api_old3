# Django/DRF imports
from django.db import models
from django.contrib.auth.models import User

# Local app imports
from hims_api.basemodel import BaseModel
from ward.models import Ward
from consultation_diagnosis.models import ConsultationDiagnosis
from person.models import Patient
from diagnosis.models import Diagnosis


class Admission ( BaseModel ):
    consultation_diagnosis = models.ForeignKey (
        ConsultationDiagnosis,
        on_delete=models.CASCADE,
        related_name="patient_admission",
    )
    diagnosis = models.ForeignKey (
        Diagnosis,
        on_delete=models.CASCADE,
        related_name="diagnosis_admission",
    )
    ward = models.ForeignKey (
        Ward, on_delete=models.PROTECT, related_name="admission_ward"
    )
    reason = models.TextField ( blank=True, null=True )
    date = models.DateTimeField ( auto_now=True )
