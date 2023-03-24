from rest_framework import serializers

from .models import FacilityCategory


class FacilityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityCategory
        fields = ["id", "name", "status"]
