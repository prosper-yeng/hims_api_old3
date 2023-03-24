from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    created_on = models.DateTimeField(default=now)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="status_created_by"
    )

    def __str__(self):
        return self.name
