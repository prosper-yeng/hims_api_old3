# Django/DRF imports
from django.db import models
from django.core.exceptions import ValidationError
from rest_framework import serializers

# Local app imports
from hims_api.basemodel import BaseModel
from status.models import Status
from room.models import Room


class Bed(BaseModel):
    number = models.CharField(max_length=255)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="status_bed",
    )
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name="room_bed")

    def __str__(self):
        return "{}".format(self.number)

    def save(self, *args, **kwargs):
        if Bed.objects.filter(number=self.number, room=self.room).exists():
            raise serializers.ValidationError(
                {
                    "message": f"Bed {self.number} already exist in Room {self.room.number}"
                }
            )
        super().save(*args, **kwargs)
