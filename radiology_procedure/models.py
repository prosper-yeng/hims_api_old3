# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from radiology_type.models import RadiologyType


class RadiologyProcedure(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    radiology_type = models.ForeignKey(
        RadiologyType,
        on_delete=models.PROTECT,
        related_name="radiology_procedure_radiology_procedure",
    )
    gdrg = models.CharField("GDRG", max_length=255, blank=True, null=True)
    icd_code = models.CharField("ICD CODE", max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
