# Django/DRF imports
from django.db import models
from rest_framework import serializers
# Local app imports
from hims_api.basemodel import BaseModel
from radiology_procedure.models import RadiologyProcedure
from sponsor.models import Sponsor
from currency_type.models import CurrencyType


class RadiologyProcedurePriceSponsor(BaseModel):
    radiology_procedure = models.ForeignKey(
        RadiologyProcedure,
        on_delete=models.PROTECT,
        related_name="radiology_procedure_price_sponsor_radiology_procedure",
    )
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.PROTECT,
        related_name="sponsor_radiology_procedure_price_sponsor",
    )
    price = models.FloatField(default=0.00)
    decription = models.TextField(blank=True, null=True)
    percentage_allowed = models.IntegerField(default=0)
    currency_type = models.ForeignKey(
        CurrencyType,
        on_delete=models.PROTECT,
        related_name="currency_type_radiology_procedure_price_sponsor",
    )

    def save(self, *args, **kwargs):
        if self.percentage_allowed > 100 or self.percentage_allowed < 0:
            return serializers.ValidationError("Bad request")
        super().save(*args, **kwargs)