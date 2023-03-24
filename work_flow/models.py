from django.db import models
from django.contrib.auth.models import User

from groups.models import Group
from service.models import Service
from choice.views import StatusChoice


class WorkFlow(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    access_level = models.IntegerField()
    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="work_flow_group",
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="work_flow_created_by"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=StatusChoice.choices)

    class Meta:
        unique_together = ("service", "group", "access_level")

    def __str__(self):
        return "{}".format(self.service)
