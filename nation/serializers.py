from rest_framework import serializers

from .models import Nation


class NationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nation
        fields = ["id", "name", "status"]
