from django.db import models
from choice.views import StatusChoice
from django.contrib.auth.models import Group, User

from status.models import Status

Group.add_to_class("is_admin", models.BooleanField(default=False))
Group.add_to_class("is_editor", models.BooleanField(default=False))
Group.add_to_class("is_viewer", models.BooleanField(default=False))
Group.add_to_class("is_superuser", models.BooleanField(default=False))
Group.add_to_class(
    "status",
    models.ForeignKey(Status, on_delete=models.CASCADE, related_name="group_status"),
)
Group.add_to_class(
    "created_by",
    models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="group_created_by",
    ),
)
