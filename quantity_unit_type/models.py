from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User

from status.models import Status


class QuantityUnitType(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    is_base_unit = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="QuantityUnitType_user"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)
