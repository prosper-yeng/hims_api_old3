# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel


class PatientType(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
