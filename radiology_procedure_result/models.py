# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from radiology_procedure_request.models import RadiologyProcedureRequest
from diagnosis.models import Diagnosis
from person.models import Staff


class RadiologyProcedureResult(BaseModel):
    radiology_procedure_request = models.ForeignKey(
        RadiologyProcedureRequest,
        on_delete=models.PROTECT,
        related_name="radiology_procedure_request_radiology_procedure_result",
    )
    # TODO: Image Files
    diagnosis = models.ForeignKey(
        Diagnosis,
        on_delete=models.PROTECT,
        related_name="diagnosis_radiology_procedure_result",
    )
    additional_comments = models.TextField()
    radiology_officer = models.ForeignKey(
        Staff,
        on_delete=models.PROTECT,
        related_name="radiology_officer_radiology_procedure_result",
    )
