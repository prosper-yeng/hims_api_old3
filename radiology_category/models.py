# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel


class RadiologyCategory(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)
