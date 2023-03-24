# Django/DRF imports
from django.db import models

# Local app imports
from hims_api.basemodel import BaseModel


class WardType(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "{}".format(self.name)
