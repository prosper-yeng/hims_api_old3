from rest_framework import serializers

from .models import Occupation


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ["id", "name", "status"]
