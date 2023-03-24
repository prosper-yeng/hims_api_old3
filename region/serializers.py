from rest_framework import serializers, fields
import datetime

from nation.serializers import NationalSerializer
from .models import Region


class RegionSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source="nation.name", required=False)

    class Meta:
        model = Region
        fields = ["id", "nation", "country_name", "name", "regional_code", "status"]


class CombinedRegionNationSerializer(serializers.ModelSerializer):
    nation = NationalSerializer(many=False)

    class Meta:
        model = Region
        fields = "__all__"
