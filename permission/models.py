from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import Permission, User
from django.utils.timezone import now

from status.models import Status

Permission.add_to_class("is_admin", models.BooleanField(default=False))
Permission.add_to_class(
    "status",
    models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="permission_status",
    ),
)
Permission.add_to_class(
    "created_by",
    models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="permission_created_by",
    ),
)
Permission.add_to_class(
    "created_on", models.DateTimeField(default=now, null=True, blank=True)
)
