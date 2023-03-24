from django.db import models
from django.contrib.auth.models import User, Group
from choice.views import StatusChoice
from person.models import Patient
from service.models import Service
from service_type.models import ServiceType
from status.models import Status


class Transaction(models.Model):
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="transaction_patient"
    )
    access_level = models.IntegerField()
    transaction_date = models.DateField(auto_now_add=True)
    assigned_group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="assigned_group",
    )
    assigned_user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="assigned_user",
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transaction_created_by"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    note = models.TextField(max_length=15000, null=True)
    modified_on = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name="transaction_modified_by",
    )
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.service)
