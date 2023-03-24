# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from consultation.models import Consultation
from radiology_procedure.models import RadiologyProcedure


class RadiologyProcedureRequest(BaseModel):
    consultation = models.ForeignKey(
        Consultation,
        on_delete=models.PROTECT,
        related_name="consultation_radiology_procedure_request",
    )
    radiology_procedure = models.ForeignKey(
        RadiologyProcedure,
        on_delete=models.PROTECT,
        related_name="radiology_procedure_radiology_procedure_request",
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
