# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from radiology_procedure_result.models import RadiologyProcedureResult
from warehouse_product.models import WarehouseProduct


class RadiologyMaterialUsed(BaseModel):
    radiology_procedure_result = models.ForeignKey(
        RadiologyProcedureResult,
        on_delete=models.PROTECT,
        related_name="radiology_procedure_result_radiology_material_used",
    )
    warehouse_product = models.ForeignKey(
        WarehouseProduct,
        on_delete=models.PROTECT,
        related_name="radiology_procedure_result_radiology_material_used",
    )
    quantity = models.IntegerField(default=0)
