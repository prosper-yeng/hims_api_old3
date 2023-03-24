from django.db import models
from django.utils.timezone import now

from choice.views import StatusChoice
from django.contrib.auth.models import User

from status.models import Status


class ServiceType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="System User"
    )
    created_on = models.DateTimeField(default=now)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)
