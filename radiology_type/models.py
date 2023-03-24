# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from radiology_category.models import RadiologyCategory


class RadiologyType(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    radiology_category = models.ForeignKey(
        RadiologyCategory,
        on_delete=models.PROTECT,
        related_name="radiology_type_radiology_category",
    )

    def __str__(self):
        return "{}".format(self.name)
