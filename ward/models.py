# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel
from ward_type.models import WardType


class Ward(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    ward_type = models.ForeignKey(
        WardType, on_delete=models.PROTECT, related_name="ward_wardtype"
    )

    def __str__(self):
        return "{}".format(self.name)
