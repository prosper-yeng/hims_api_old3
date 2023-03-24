from rest_framework import serializers

from region.serializers import RegionSerializer, CombinedRegionNationSerializer
from .models import District


class DistrictSerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source="region.name", required=False)

    class Meta:
        model = District
        fields = ["id", "name", "region", "region_name", "status"]


class CombinedDistrictRegionSerializer(serializers.ModelSerializer):
    region = CombinedRegionNationSerializer(many=False)

    class Meta:
        model = District
        fields = "__all__"
