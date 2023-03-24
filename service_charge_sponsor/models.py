from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User
from service.models import Service
from currency_type.models import CurrencyType
from sponsor.models import Sponsor
from status.models import Status


class ServiceChargeSponsor(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_allowed = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    currency_type = models.ForeignKey(CurrencyType, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.service)
