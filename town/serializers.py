from rest_framework import serializers

from district.serializers import DistrictSerializer, CombinedDistrictRegionSerializer
from .models import Town


class TownSerializer(serializers.ModelSerializer):
    # district_name = serializers.CharField ( source='district.name_of_district', required=False )
    class Meta:
        model = Town
        fields = ["id", "district", "name", "created_on", "status"]


class CombinedTownDistrictSerializer(serializers.ModelSerializer):
    district = CombinedDistrictRegionSerializer(many=False)

    class Meta:
        model = Town
        fields = "__all__"
