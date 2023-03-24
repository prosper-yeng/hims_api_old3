from datetime import datetime
import ipaddress

import django
from django.contrib.auth.models import User
from django.utils.timezone import now

from attendance_type.models import AttendanceType

from django.db import models


# Create your models here.
from clinic_type.models import ClinicType
from consulting_room.models import ConsultingRoom
from person.models import Patient
from service.models import Service
from sponsor.models import Sponsor
from status.models import Status
from transaction.models import Transaction


class SponsorServicePrice(models.Model):
    sponsor = models.ForeignKey(
        Sponsor, on_delete=models.CASCADE, related_name="sponsor_service_price"
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="sponsor_service"
    )
    amount_allowed = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_allowed = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="sponsor User"
    )
    created_on = models.DateTimeField(default=now)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="sponsor_service_status"
    )

    def __str__(self):
        return "{}".format(self.service)
