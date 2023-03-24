from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User
from service.models import Service
from currency_type.models import CurrencyType
from status.models import Status


class ServiceCharge(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE)
    price = models.FloatField()
    currency_type = models.ForeignKey(CurrencyType, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.service)
