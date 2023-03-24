from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import User
from service_type.models import ServiceType
from status.models import Status


class Service(models.Model):
    service_type = models.ForeignKey(
        ServiceType,
        on_delete=models.CASCADE,
        help_text="eg. Opd services, Pharmacy, Laboratory, Inpatient etc",
    )
    name = models.CharField(
        max_length=250,
        unique=True,
        help_text="eg. registration, consultation, medicine, lab test, anastezia, procedure etc",
    )
    description = models.CharField(max_length=250, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)
