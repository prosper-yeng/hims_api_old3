from rest_framework import serializers

from .models import ConsultingRoom

ConsultingRoom


class ConsultingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultingRoom
        fields = ["id", "name", "status", "created_by"]

        read_only_fields = ("id",)
