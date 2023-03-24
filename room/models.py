# Django/DRF imports
from django.db import models
from rest_framework import serializers

# Local app imports
from hims_api.basemodel import BaseModel
from ward.models import Ward


class Room(BaseModel):
    number = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    ward = models.ForeignKey(Ward, on_delete=models.PROTECT, related_name="ward_room")

    def __str__(self):
        return f" room: {self.number} (ward: {self.ward.name})"

    def save(self, *args, **kwargs):
        if Room.objects.filter(number=self.number, ward=self.ward).exists():
            raise serializers.ValidationError(
                {
                    "message": f"Room {self.number} already exist in {self.ward.name} Ward"
                }
            )
        super().save(*args, **kwargs)
