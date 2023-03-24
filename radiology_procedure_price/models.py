# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from radiology_procedure.models import RadiologyProcedure
from currency_type.models import CurrencyType


class RadiologyProcedurePrice(BaseModel):
    radiology_procedure = models.ForeignKey(
        RadiologyProcedure,
        on_delete=models.PROTECT,
        related_name="radiology_procedure_radiology_procedure",
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    currency_type = models.ForeignKey(
        CurrencyType,
        on_delete=models.PROTECT,
        related_name="currency_type_radiology_procedure_price",
    )
